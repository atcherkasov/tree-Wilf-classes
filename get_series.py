from parsers import parser
import parallel_setup


def equations_to_series(equations: list, n: int, xy_equation=True):
    """
    метод принимает на вход массив уравнений одной системы и желаемую длину ряда
    метод возвращает разложение функции F(x, y) в ряд по x
    """
    from my_poly_functions import add, make_equation

    x = [[1], [0]]

    variable = {}
    f = add(x, [[0]])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [[0]]

    for i in range(1, n - 1):
        arguments = []
        for j in range(1, len(variable)):
            arguments.append([variable[equations[j - 1][1]],
                              variable[equations[j - 1][2]],
                              variable[equations[j - 1][3]],
                              variable[equations[j - 1][4]], n])
        result = parallel_setup.pool.map(make_equation, arguments)

        for j in range(len(variable) - 1):
            variable[j + 1] = result[j]

        f = add(x, variable[1])
        variable[0] = f

    new_a = make_equation([variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]], n + 1],
                          xy_equation)
    a = new_a
    f = add(x, a)
    cut_f = f[(-2 * n):]
    return cut_f


def combo_equations_to_series(equations: list, n: int):
    """
    этот метод нужен для получения функции разложения G(x) в ряд
    он просто вызывает метод equations_to_series;
    получает из F(x, y) G(x);
    и возвражает ОБА разложения в ряд;
    """
    xy_series = equations_to_series(equations, n)
    x_series = []
    for poly in xy_series:
        x_series.append([poly[-1]])
    return x_series, xy_series


def beautiful_time(all_time):
    hours = all_time // 3600
    all_time %= 3600
    minutes = all_time // 60
    seconds = round(all_time % 60, 3)
    return str(hours) + ' часов, ' + str(minutes) + ' минут, ' + str(
        seconds) + ' секунд.'


if __name__ == '__main__':
    from my_poly_functions import show_global
    import time

    parallel_setup.init()

    start = time.time()
    groups, leaf_number = parser('input_files/short_equations_10.txt')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    n = 13  # длина ряда!!!
    test_mode = True  # тестовый режим активирован?
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if test_mode:
        file = open(
            'rubbish_files/short_nice_series_' + leaf_number + '_' + str(n) + '.txt',
            'w')
        loges_file = open(
            'rubbish_files/test_short_time_per_percents_' + leaf_number + '_' + str(n) + '.txt',
            'w')
    else:
        file = open(
            'output_files/short_nice_series_' + leaf_number + '_' + str(n) + '.txt',
            'w')
        loges_file = open(
            'loges/short_time_per_percents_' + leaf_number + '_' + str(n) + '.txt',
            'w')
    size = len(groups)

    part = 5
    part_time = part
    for i in range(size):
        x_series, xy_series = combo_equations_to_series(groups[i][1:], (n + 1) // 2)
        print(groups[i][0][:-1], file=file)
        print(show_global(x_series), file=file)
        print(show_global(xy_series) + '\n', file=file)
        """
        этот кусок кода в среднем работает за 16 сек, в то врем как кусок кода выше
        работает за 8 сек (он алгоритмически в два раза быстрее)
        # seriesXY = equations_to_series(groups[i][1:], 6)
        # seriesX = equations_to_series(groups[i][1:], 6, False)
        # print(groups[i][0][:-1], file=file)
        # print(show(seriesX), file=file)
        # print(show(seriesXY) + '\n', file=file)
        # 16 sec 
        """
        percent = round(i / float(size) * 100, 3)
        if percent >= part_time:
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start), file=loges_file)
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start))

            part_time += part
        else:
            print(percent, '%')
    file.close()

    print('                заняло ' + beautiful_time(time.time() - start),
          file=loges_file)
    print('заняло ' + beautiful_time(time.time() - start))
    loges_file.close()

from source.parsers import parser
from source import parallel_setup


def equations2series(equations: list, n: int, xy_equation=True):
    """
    метод принимает на вход массив уравнений одной системы и желаемую длину ряда
    метод возвращает разложение функции F(x, y) в ряд по x
    """
    from source.poly_func.my_poly_functions import add_global, make_equation

    x = [[1], [0]]

    variable = {}
    f = add_global(x, [[0]])
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
        # result = parallel_setup.pool.map(make_equation, arguments)
        result = [make_equation(args) for args in arguments]
        for j in range(len(variable) - 1):
            variable[j + 1] = result[j]

        f = add_global(x, variable[1])
        variable[0] = f

    new_a = make_equation([variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]], n + 1],
                          xy_equation)
    a = new_a
    f = add_global(x, a)
    cut_f = f[(-2 * n):]
    return cut_f


def equations2series_y(equations: list, n: int, y_pow: int, xy_equation=True):
    """
    метод принимает на вход массив уравнений одной системы и желаемую длину ряда
    метод возвращает разложение функции F(x, y) в ряд по x
    """
    from source.poly_func.my_poly_functions import add_global, make_equation_cut

    x = [[1], [0]]

    variable = {}
    f = add_global(x, [[0]])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [[0]]
    for i in range(1, n - 1):
        arguments = []
        for j in range(1, len(variable)):
            arguments.append([variable[equations[j - 1][1]],
                              variable[equations[j - 1][2]],
                              variable[equations[j - 1][3]],
                              variable[equations[j - 1][4]], n, y_pow])
        result = parallel_setup.pool.map(make_equation_cut, arguments)

        for j in range(len(variable) - 1):
            variable[j + 1] = result[j]

        f = add_global(x, variable[1])
        variable[0] = f

    new_a = make_equation_cut([variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]], n + 1, y_pow],
                          xy_equation)
    a = new_a
    f = add_global(x, a)
    cut_f = f[(-2 * n):]
    return cut_f


def combo_equations_to_series(equations: list, args: list):
    """
    этот метод нужен для получения функции разложения G(x) в ряд
    он просто вызывает метод equations_to_series;
    получает из F(x, y) G(x);
    и возвражает ОБА разложения в ряд;
    """
    if len(args) == 1:
        xy_series = equations2series(equations, args[0])
    elif len(args) == 2:
        xy_series = equations2series_y(equations, args[0], args[1])
    else:
        print('ERROR')
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
    from source.poly_func.my_poly_functions import show_global
    import time

    parallel_setup.init()

    start = time.time()
    groups, leaf_number = parser('input_files/equations_short_10.txt')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    x_len = 151  # длина ряда!!!
    y_len = 2
    test_mode = False  # тестовый режим активирован?
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if test_mode:
        file = open(
            'rubbish_files/short_nice_series_' + leaf_number + '_' + str(x_len) + '_' + str(y_len) + '.txt',
            'w')
        loges_file = open(
            'rubbish_files/log_short_' + leaf_number + '_' + str(x_len) + '_' + str(y_len) + '.txt',
            'w')
    else:
        file = open(
            'output_files/series_short_' + leaf_number + '_' + str(x_len) + '_' + str(y_len) + '.txt',
            'w')
        loges_file = open(
            'loges/log_short_' + leaf_number + '_' + str(x_len) + '_' + str(y_len) + '.txt',
            'w')
    size = len(groups)

    part = 2.5
    part_time = part
    for i in range(size):
        x_series, xy_series = combo_equations_to_series(groups[i][1:], [(x_len + 1) // 2, y_len])
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
        percent = round(i / float(size) * 100, 1)
        if percent >= part_time:
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start), file=loges_file)
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start))

            part_time += part
        else:
            print(percent, '%')
    file.close()

    print(' ВЕСЬ ПРОЦЕСС ЗАНЯЛ: ' + beautiful_time(time.time() - start),
          file=loges_file)
    print('заняло ' + beautiful_time(time.time() - start))
    loges_file.close()

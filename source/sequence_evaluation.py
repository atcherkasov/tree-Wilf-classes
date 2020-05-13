from source import parallel_setup


def compute_sequence(equations: list, n: int):
    """
    метод принимает на вход массив уравнений одной системы и желаемую длину ряда
    метод возвращает разложение функции F(x, y) в ряд по x
    """
    from source.poly_func.my_poly_functions import add_local, x_equation

    x = [1, 0]

    variable = {}
    f = add_local(x, [0])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [0]

    for i in range(1, n - 1):
        arguments = []
        for j in range(1, len(variable)):
            arguments.append([variable[equations[j - 1][1]],
                              variable[equations[j - 1][2]],
                              variable[equations[j - 1][3]],
                              variable[equations[j - 1][4]], n])
        result = parallel_setup.pool.map(x_equation, arguments)

        for j in range(len(variable) - 1):
            variable[j + 1] = result[j]

        f = add_local(x, variable[1])
        variable[0] = f

    new_a = x_equation([variable[equations[0][1]], variable[equations[0][2]],
                        variable[equations[0][3]], variable[equations[0][4]], n + 1])
    a = new_a
    f = add_local(x, a)
    cut_f = f[(-2 * n):]
    return cut_f


if __name__ == '__main__':
    from source.poly_func.my_poly_functions import show_local
    from source.parsers import parser
    import time
    from source.get_series import beautiful_time

    parallel_setup.init()

    start = time.time()
    groups, leaf_number = parser('../input_files/equations_short_9.txt')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    x_len = 151  # длина ряда!!!
    test_mode = True  # тестовый режим активирован?
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if test_mode:
        file = open(
            '../rubbish_files/short_x_' + leaf_number + '_' + str(x_len) + '.txt',
            'w')
        loges_file = open(
            '../rubbish_files/log_x_' + leaf_number + '_' + str(x_len) + '.txt',
            'w')
    else:
        file = open(
            '../output_files/series_x_' + leaf_number + '_' + str(x_len) + '.txt',
            'w')
        loges_file = open(
            '../loges/log_x_' + leaf_number + '_' + str(x_len) + '.txt',
            'w')
    size = len(groups)

    part = 2.5
    part_time = part
    for i in range(size):
        x_series = compute_sequence(groups[i][1:], (x_len + 1) // 2)
        print(groups[i][0][:-1], file=file)
        print(show_local(x_series, loc='x'), file=file)

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

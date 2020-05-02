# coding=utf8
from source.parsers import parser
from source.get_series import beautiful_time, equations_to_series


def decomposition_series_to_y(equations: list, n: int, xy_series=None):
    """

    """
    if xy_series == None:
        xy_series = equations_to_series(equations, n)
    max_pow = max([len(poly) for poly in xy_series]) - 1   # максимальная степень при y
    yx_series = []
    for pow in range(max_pow, -1, -1):
        new_poly = []
        for poly in xy_series:
            if len(poly) >= pow + 1:
                new_poly.append(poly[-pow - 1])
            else:
                new_poly.append(0)
        yx_series.append(new_poly)

    return yx_series


if __name__ == '__main__':
    from source.my_poly_functions import show_global
    import time
    from source import parallel_setup

    parallel_setup.init()

    start = time.time()
    groups, leaf_number = parser('input_files/equations_short_4.txt')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    n = 33  # длина ряда!!!
    test_mode = True  # тестовый режим активирован?
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    if test_mode:
        file = open(
            'rubbish_files/y_short_nice_series_' + leaf_number + '_' + str(n) + '.txt',
            'w')
        loges_file = open(
            'loges/test_short_time_per_percents_' + leaf_number + '_' + str(n) + '.txt',
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
        yx_series = decomposition_series_to_y(groups[i][1:], (n + 1) // 2)
        print(groups[i][0][:-1], file=file)
        print(show_global(yx_series, glob='y', loc='x') + '\n', file=file)
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

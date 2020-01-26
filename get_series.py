import numpy as np
from poly_functions import add, make_equlation, show
from parsers import parser


def equations_to_series(equations: list, n: int, xy_equation=True):
    x = [np.poly1d([1]), np.poly1d([0])]

    variable = {}
    f = add(x, [np.poly1d([0])])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [np.poly1d([0])]

    for i in range(1, n - 1):
        new_variable = {}
        for j in range(1, len(variable)):
            new_variable[j] = make_equlation(variable[equations[j - 1][1]],
                                             variable[equations[j - 1][2]],
                                             variable[equations[j - 1][3]],
                                             variable[equations[j - 1][4]],
                                             xy_equation)
        for j in range(1, len(variable)):
            variable[j] = new_variable[j]

        f = add(x, variable[1])
        variable[0] = f

    new_a = make_equlation(variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]],
                           xy_equation)
    a = new_a
    f = add(x, a)
    cut_f = f[(-2 * i - 4):]
    return cut_f


def combo_equations_to_series(equations: list, n: int):
    xy_series = equations_to_series(equations, n)
    x_series = []
    for poly in xy_series:
        x_series.append(np.poly1d([poly[0]]))
    return x_series, xy_series


if __name__ == '__main__':
    import time
    start = time.time()
    groups = parser()

    file = open('../series.txt', 'w')
    size = len(groups)
    for i in range(size):
        x_series, xy_series = combo_equations_to_series(groups[i][1:], 7)
        print(groups[i][0][:-1], file=file)
        print(show(x_series), file=file)
        print(show(xy_series) + '\n', file=file)
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
        print(int(i / float(size) * 100), '%')
    file.close()
    print('ALL TIME:', time.time() - start)
import numpy as np
from poly_functions import add, make_equlation, show
from parsers import parser
import sympy as sp

def equations_to_series(equations: list, n: int, xy_equation=True):
    x = sp.Symbol('x')
    y = sp.Symbol('y')

    variable = {}
    f = x + 0
    variable['F'] = f

    # присваиваем всем левым частям равенства (т. е. всем переменным кроме F значение 0)
    for i in range(len(equations)):
        variable[equations[i][0]] = 0

    # в цикле "удлинняем" ряды всех переменных
    for i in range(1, n - 1):
        new_variable = {}
        for j in range(len(equations)):
            # if j != 'F':
                # new_variable[j] = make_equlation(variable[equations[j - 1][1]],
                #                                  variable[equations[j - 1][2]],
                #                                  variable[equations[j - 1][3]],
                #                                  variable[equations[j - 1][4]],
                #                                  xy_equation)
#             print(j, equations[j][0], equations[j][1], equations[j][2], equations[j][3], equations[j][4])
            new_variable[equations[j][0]] =x * (variable[equations[j][1]] *\
                              variable[equations[j][2]] + (y - 1) * \
                              variable[equations[j][3]] * \
                              variable[equations[j][4]])
#         print(new_variable)
        for j in variable:
            if j != 'F':
                variable[j] = new_variable[j]
        f = x + variable['a1']
        variable['F'] = f

    new_a = x * (variable[equations[0][1]] * variable[equations[0][2]] + (y - 1) * \
            variable[equations[0][3]] * variable[equations[0][4]])
    a = new_a
    f = x + a
    f = sp.collect(sp.expand(f), x)
    f = f.args[:n] #, x #.args[:n]
    return f
#     cut_f = f[(-2 * i - 4):]
#     return cut_f


# TODO:  переделать
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
        x_series, xy_series = combo_equations_to_series(groups[i][1:], 9)
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

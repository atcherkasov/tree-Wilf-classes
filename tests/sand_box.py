# from source.get_series import equations2series, equations2series_y
from source.poly_func.my_poly_functions import show_global, make_equation_cut, make_equation
from source import parallel_setup

sum_x = 0.0
sum_y = 0.0


def equations2series(equations: list, n: int, xy_equation=True):
    """
    метод принимает на вход массив уравнений одной системы и желаемую длину ряда
    метод возвращает разложение функции F(x, y) в ряд по x
    """
    global sum_x
    from source.poly_func.my_poly_functions import add_global, make_equation
    from time import time

    x = [[1], [0]]

    variable = {}
    f = add_global(x, [[0]])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [[0]]

    s1 = time()
    for i in range(1, n - 1):
        arguments = []
        s2 = time()
        for j in range(1, len(variable)):
            arguments.append([variable[equations[j - 1][1]],
                              variable[equations[j - 1][2]],
                              variable[equations[j - 1][3]],
                              variable[equations[j - 1][4]], n])
        s3 = time()

        # print('prepare x:', s3 - s2, 'размер:', len(arguments))
        # sum_x += s3 - s2
        # print(arguments)
        result = parallel_setup.pool.map(make_equation, arguments)
        s4 = time()
        print('result x:', s4 - s3)
        sum_x += s4 - s3


        for j in range(len(variable) - 1):
            variable[j + 1] = result[j]

        f = add_global(x, variable[1])
        variable[0] = f

    new_a = make_equation([variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]], n + 1],
                          xy_equation)
    print('цикл x занял:', time() - s1)
    a = new_a
    f = add_global(x, a)
    cut_f = f[(-2 * n):]
    print('\nsum_x:', sum_x)
    return cut_f


def equations2series_y(equations: list, n: int, y_pow: int, xy_equation=True):
    """
    метод принимает на вход массив уравнений одной системы и желаемую длину ряда
    метод возвращает разложение функции F(x, y) в ряд по x
    """
    from source.poly_func.my_poly_functions import add_global, make_equation_cut
    from time import time
    global sum_y

    x = [[1], [0]]

    variable = {}
    f = add_global(x, [[0]])
    variable[0] = f

    for i in range(len(equations)):
        variable[equations[i][0]] = [[0]]
    s1 = time()
    for i in range(1, n - 1):
        arguments = [None] * (len(variable) - 1)
        s2 = time()
        for j in range(1, len(variable)):
            arguments[j - 1] = ([variable[equations[j - 1][1]],
                              variable[equations[j - 1][2]],
                              variable[equations[j - 1][3]],
                              variable[equations[j - 1][4]], n, y_pow])
        s3 = time()
        # sum_y += s3 - s2
        # print('prepare y:', s3 - s2, 'размер:', len(arguments))
        # print(arguments)
        result = parallel_setup.pool.map(make_equation_cut, arguments)
        s4 = time()
        print('result y:', s4 - s3)
        sum_y += s4 - s3

        for j in range(len(variable) - 1):
            variable[j + 1] = result[j]

        f = add_global(x, variable[1])
        variable[0] = f

    new_a = make_equation_cut([variable[equations[0][1]], variable[equations[0][2]],
                           variable[equations[0][3]], variable[equations[0][4]], n + 1, y_pow],
                          xy_equation)
    print('цикл y занял:', time() - s1)
    a = new_a
    f = add_global(x, a)
    cut_f = f[(-2 * n):]
    print('\nsum_y:', sum_y)

    return cut_f





if __name__ == '__main__':
    from time import time
    arr = [[1, 0, 0, 2, 0],
           [2, 0, 1, 2, 1]]

    n = 65

    parallel_setup.init()

    s1 = time()
    # print(show_global(equations2series(arr, (n + 1) // 2)))
    # print(time() - s1)
    # s2 = time()
    # print(show_global(equations2series_y(arr, (n + 1) // 2, 3)))
    # print(time() - s2)

    print('\n>>>>>>>>>>>>>>>>>>\n')
    # arr = [[1, 0, 0, 2, 0],
    #        [2, 3, 0, 2, 0],
    #        [3, 4, 0, 2, 0],
    #        [4, 5, 0, 2, 0],
    #        [5, 1, 0, 2, 0]]

    # arr = [[1, 0, 0, 2, 0],
    #         [2, 3, 1, 4, 1],
    #         [3, 5, 0, 6, 0],
    #         [4, 7, 1, 8, 1],
    #         [5, 9, 0, 10, 0],
    #         [6, 11, 1, 12, 1],
    #         [7, 13, 0, 14, 0],
    #         [8, 15, 1, 16, 1],
    #         [9, 17, 0, 2, 0],
    #         [10, 18, 1, 4, 1],
    #         [11, 19, 0, 6, 0],
    #         [12, 20, 1, 8, 1],
    #         [13, 21, 0, 10, 0],
    #         [14, 22, 1, 12, 1],
    #         [15, 23, 0, 14, 0],
    #         [16, 24, 1, 16, 1],
    #         [17, 0, 1, 2, 1],
    #         [18, 5, 1, 6, 1],
    #         [19, 9, 1, 10, 1],
    #         [20, 13, 1, 14, 1],
    #         [21, 17, 1, 2, 1],
    #         [22, 19, 1, 6, 1],
    #         [23, 21, 1, 10, 1],
    #         [24, 23, 1, 14, 1]]

    arr = [
        [1, 0, 0, 2, 0],
        [2, 3, 0, 2, 0],
        [3, 4, 0, 2, 0],
        [4, 5, 0, 2, 0],
        [5, 6, 0, 2, 0],
        [6, 7, 0, 2, 0],
        [7, 1, 0, 2, 0]
    ]
    s1 = time()
    print(show_global(equations2series(arr, (n + 1) // 2)))
    print(time() - s1)
    print('\n\n')
    s2 = time()
    print(show_global(equations2series_y(arr, (n + 1) // 2, 3)))
    print(time() - s2)

    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

    s1 = time()
    print(make_equation([[[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]],
                         [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]],
                         [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]],
                         [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]], 11]))
    print(time() - s1)
    print('\n')
    s2 = time()
    print(make_equation_cut([ [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]],
                              [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]],
                              [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]],
                              [[1, 3], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1]], 11, 2]))
    print(time() - s2)

    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

    arg = [[[2, 4, 1, 5, 3, 10, 4], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1, 5, 100, 3, 6, 4]],
             [[2, 4, 1, 7, 3, 10, 4], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1, 5, 100, 3, 6, 4]],
             [[2, 4, 1, 5, 500, 10, 4], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1, 5, 100, 3, 6, 4]],
             [[2, 4, 1, 5, 3, 10, 4], [2, 4, 1, 5, 3, 10, 4], [3, 5, 1, 5, 100, 3, 6, 4]], 11]

    s1 = time()
    print(make_equation(arg))
    print(time() - s1)
    print('\n')
    s2 = time()
    print(make_equation_cut(arg + [3]))
    print(time() - s2)

    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

    from multiprocessing import Pool, cpu_count
    dead_pool = Pool()
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    n = 10
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    args = [arg for i in range(n)]
    s1 = time()
    print(dead_pool.map(make_equation, args))

    print(time() - s1)
    print('\n')
    args_cut = [arg + [3] for i in range(n)]

    s2 = time()

    print(dead_pool.map(make_equation_cut, args_cut))
    print(time() - s2)

from source.get_series import equations2series, equations2series_y
from source.poly_func.my_poly_functions import show_global
from source import parallel_setup


if __name__ == '__main__':
    from time import time
    arr = [[1, 0, 0, 2, 0],
           [2, 0, 1, 2, 1]]

    n = 13

    parallel_setup.init()

    s1 = time()
    print(show_global(equations2series_y(arr, (n + 1) // 2, 1)))
    print(time() - s1)
    s2 = time()
    print(show_global(equations2series(arr, (n + 1) // 2)))
    print(time() - s2)

    arr = [[1, 0, 0, 2, 0],
           [2, 3, 0, 2, 0],
           [3, 4, 0, 2, 0],
           [4, 5, 0, 2, 0],
           [5, 1, 0, 2, 0]]
    s1 = time()
    print(show_global(equations2series_y(arr, (n + 1) // 2, 1)))
    print(time() - s1)
    s2 = time()
    print(show_global(equations2series(arr, (n + 1) // 2)))
    print(time() - s2)

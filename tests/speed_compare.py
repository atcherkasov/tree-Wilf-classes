from source.parsers import parser
from source import parallel_setup
from time import time


def compare_speed(f1, f2, x_len, y_len, path='../input_files/equations_short_9.txt'):
    groups, leaf_number = parser(path)
    # groups, leaf_number = parser('input_files/equations_short_9.txt')

    size = len(groups)
    cnt = 0
    for i in range(size):
        s1 = time()
        xy_series = f1(groups[i][1:], (x_len + 1) // 2)
        time_1 = time() - s1
        # print(res_1)
        s2 = time()
        xy_series = f2(groups[i][1:], (x_len + 1) // 2, y_len)
        time_2 = time() - s2
        if time_1 <= time_2:
            print(i)
            cnt += 1
    print(cnt, size)
    print(size / cnt)
        # print()


if __name__ == '__main__':
    from source.get_series import equations2series, equations2series_y
    parallel_setup.init()
    compare_speed(equations2series, equations2series_y, 33, 3)

    # from os import listdir
    # from os.path import isfile, join
    #
    # onlyfiles = [f for f in listdir('') if isfile(join('', f))]
    # print(*onlyfiles)
    # import os
    #
    # arr = os.listdir()
    # print(arr)

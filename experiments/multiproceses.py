from multiprocessing import Pool


def doubler(number):
    return number ** 3


if __name__ == '__main__':
    # numbers = [5, 10, 20]
    # pool = Pool(processes=3)
    # print(pool.map(doubler, numbers))
    import random

    arr = [random.randint(10 ** 6, 10 ** 8) for i in range(10 ** 6)]
    import time


    pool = Pool()

    start = time.time()

    result = pool.map(doubler, arr)

    print(result[0])

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # for i in range(len(arr)):
    #     arr[i] = doubler(arr[i])
    # print(arr[0])

    print(time.time() - start)
import numpy as np
from numba import guvectorize, int64, vectorize, float64

# 'void(double[:], double[:], double[:])'
# [(int64[:], int64[:], int64[:])]
# 'void(int64[:], int64[:], int64[:])'
@guvectorize([(int64[:], int64[:], int64[:])], '(n), (n)->(n)')#, target='cuda')
def multiplication(a, b, res):
    # res = np.zeros(len(a))
    for i in range(len(a)):
        res[i] = a[i] * b[i]


N = 9
a = [10**N]
b = [10**N]
res = [0]

size = 10 ** 3
A = np.array([a for i in range(size)])
B = np.array([b for i in range(size)])
Res = np.array([res for i in range(size)])
multiplication(A, B, Res)
print(len(str(Res[0][0])) - 1)
print(Res[0][0])
print(10**N * 10**N)

# @vectorize([float64[:](float64[:], float64)[:]])
# def f(x, y):
#     return x + y
#
# a = np.arange(6)
# b = np.arange(6)
# kek = np.array([a, b])
# c = np.arange(6)
# d = np.arange(6)
# lol = np.array([c, d])
# print(f(lol, kek))
#
# print(np.array([1, 3, 2]) * np.array([1, 3, 2, 1]))
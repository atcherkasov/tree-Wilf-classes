from array import array

import numpy as np
from poly_functions import show_y, show, mult, add

# тест функции show_y
assert show_y(np.poly1d([2, 1, 3])) == '(2*y^2 + y^1 + 3)'
assert show_y(np.poly1d([2, 0, 0])) == '(2*y^2)'
assert show_y(np.poly1d([0, 3, 0])) == '(3*y^1)'
assert show_y(np.poly1d([0, 0, 0])) == '()'
assert show_y(np.poly1d([0])) == '()'
assert show_y(np.poly1d([3])) == '(3)'
assert show_y(np.poly1d([0, 0, 3])) == '(3)'

# тест функции show
assert show([np.poly1d([2, 1, 3]), np.poly1d([0]), np.poly1d([1, 2])]) == \
       '(2*y^2 + y^1 + 3)*x^2 + (y^1 + 2)'

# тест функции mult
a = [[2,3,1], [2,1], [1,0], [3,1]]
b = [[0], [0], [1,1], [4,3]]
assert mult(a, b) == [np.poly1d([0.]), np.poly1d([0.]), np.poly1d([2., 5., 4., 1.]),
         np.poly1d([8., 20., 16., 4.]), np.poly1d([9., 11., 3.]),
         np.poly1d([7., 7., 1.]), np.poly1d([12., 13., 3.])]

# тест функции add
a = [[2,3,1], [2,1], [1,0], [3,1]]
b = [[0], [0], [0], [0], [1,1], [4,3]]
res = add(a, b)
ans = [[0], [0], np.array([2, 3, 1]), np.array([2, 1]), np.array([2, 1]),
       np.array([7, 4])]

assert len(ans) == len(res)
for i in range(len(res)):
    assert len(res[i]) == len(ans[i])
    for j in range(len(res[i])):
        assert res[i][j] == ans[i][j]

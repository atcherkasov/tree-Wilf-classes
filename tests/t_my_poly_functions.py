# coding=utf8
from my_poly_functions import show_local, show_global, mult_y, mult, add_y, add


# тест функции show_local
assert show_local([2, 1, 3]) == '(2*y^2 + y^1 + 3)'
assert show_local([2, 0, 0]) == '(2*y^2)'
assert show_local([0, 3, 0]) == '(3*y^1)'
assert show_local([0, 0, 0]) == '()'
assert show_local([0]) == '()'
assert show_local([3]) == '(3)'
assert show_local([0, 0, 3]) == '(3)'
assert show_local([2, 1, 3], loc='z') == '(2*z^2 + z^1 + 3)'
assert show_local([2, 0, 0], loc='z') == '(2*z^2)'
assert show_local([0, 3, 0], loc='z') == '(3*z^1)'

print('show_local PASSED!\n')

# тест функции show_global
assert show_global([[2, 1, 3], [0], [1, 2]]) == \
       '(2*y^2 + y^1 + 3)*x^2 + (y^1 + 2)'
assert show_global([[2, 1, 3], [0], [1, 2]], glob='a', loc='b') == \
       '(2*b^2 + b^1 + 3)*a^2 + (b^1 + 2)'

print('show PASSED!\n')

# тест функции add_y
assert add_y([3, 5, 1, 4, 3], [2, 4, 2]) == [3, 5, 3, 8, 5]
assert add_y([0, 0, 3, 5, 1, 4, 3], [0, 2, 4, 2]) == [3, 5, 3, 8, 5]
assert add_y([2, 4, 2], [3, 5, 1, 4, 3]) == [3, 5, 3, 8, 5]
assert add_y([0, 0, 2, 4, 2], [0, 0, 3, 5, 1, 4, 3]) == [3, 5, 3, 8, 5]
assert add_y([1, 4], [0]) == [1, 4]

print('add_y PASSED!\n')

# тест функции add
a = [[2, 3, 1], [2, 1], [1, 0], [3, 1]]
b = [[0], [0], [0], [0], [1, 1], [4, 3]]
assert add(a, b) == [[0], [0], [2, 3, 1], [2, 1], [2, 1], [7, 4]]
print('add PASSED!\n')

# тест функции mult_y
a1 = [3, 2, 1]
b1 = [1, 1]
assert mult_y(a1, b1) == [3, 5, 3, 1]
a1 = [0, 0, 3, 2, 1]
b1 = [0, 1, 1]
assert mult_y(a1, b1) == [3, 5, 3, 1]
print('mylt_y PASSED!\n')

# тест функции mult
a = [[2, 3, 1], [2, 1], [1, 0], [3, 1]]
b = [[2], [1], [1, 1], [4, 3]]
assert mult(a, b, 10) == [[4, 6, 2], [2, 7, 3], [2, 5, 8, 2], [8, 20, 23, 6],
                          [9, 14, 4], [7, 7, 1], [12, 13, 3]]
assert mult(a, b, 7) == [[4, 6, 2], [2, 7, 3], [2, 5, 8, 2], [8, 20, 23, 6],
                          [9, 14, 4], [7, 7, 1], [12, 13, 3]]
b[0] = [0]
b[1] = [0]
assert mult(a, b, 10) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult(a, b, 7) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult(a, b, 6) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult(a, b, 5) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult(a, b, 4) == [[8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult(a, b, 3) == [[9, 11, 3], [7, 7, 1], [12, 13, 3]]

print('mult PASSED!\n')

print('ALL TESTS PASSED!')
# coding=utf8
from source.poly_func.my_poly_functions import show_local, show_global, mult_local, mult_global, \
    add_local, add_global, mult_y


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

# тест функции add_local
assert add_local([3, 5, 1, 4, 3], [2, 4, 2]) == [3, 5, 3, 8, 5]
assert add_local([0, 0, 3, 5, 1, 4, 3], [0, 2, 4, 2]) == [3, 5, 3, 8, 5]
assert add_local([2, 4, 2], [3, 5, 1, 4, 3]) == [3, 5, 3, 8, 5]
assert add_local([0, 0, 2, 4, 2], [0, 0, 3, 5, 1, 4, 3]) == [3, 5, 3, 8, 5]
assert add_local([1, 4], [0]) == [1, 4]

print('add_local PASSED!\n')

# тест функции add_global
a = [[2, 3, 1], [2, 1], [1, 0], [3, 1]]
b = [[0], [0], [0], [0], [1, 1], [4, 3]]
assert add_global(a, b) == [[0], [0], [2, 3, 1], [2, 1], [2, 1], [7, 4]]
print('add PASSED!\n')

# тест функции mult_local
a1 = [3, 2, 1]
b1 = [1, 1]
assert mult_local(a1, b1, 10) == [3, 5, 3, 1]

a1 = [0, 0, 3, 2, 1]
b1 = [0, 1, 1]
assert mult_local(a1, b1, 10) == [3, 5, 3, 1]

a1 = [5, 2, 7, 2]
b1 = [3, 3, 3]
assert mult_local(a1, b1, 2) == [33, 27, 6]
assert mult_local(b1, a1, 2) == [33, 27, 6]
assert mult_local(a1, b1, 0) == [6]
assert mult_local(a1, b1, 5) == [15, 21, 42, 33, 27, 6]
assert mult_local(a1, b1, 4) == [21, 42, 33, 27, 6]

print('mylt_local PASSED!\n')

# тест функции mult_y
a1 = [3, 2, 1]
b1 = [1, 1]
assert mult_y(a1, b1) == [3, 5, 3, 1]

a1 = [0, 0, 3, 2, 1]
b1 = [0, 1, 1]
assert mult_y(a1, b1) == [3, 5, 3, 1]

a1 = [5, 2, 7, 2]
b1 = [3, 3, 3]
assert mult_y(a1, b1) == [15, 21, 42, 33, 27, 6]

print('mylt_y PASSED!\n')


# тест функции mult_global
a = [[2, 3, 1], [2, 1], [1, 0], [3, 1]]
b = [[2], [1], [1, 1], [4, 3]]
assert mult_global(a, b, 10, 10) == [[4, 6, 2], [2, 7, 3], [2, 5, 8, 2], [8, 20, 23, 6],
                          [9, 14, 4], [7, 7, 1], [12, 13, 3]]
assert mult_global(a, b, 7, 10) == [[4, 6, 2], [2, 7, 3], [2, 5, 8, 2], [8, 20, 23, 6],
                          [9, 14, 4], [7, 7, 1], [12, 13, 3]]
b[0] = [0]
b[1] = [0]
assert mult_global(a, b, 10, 10) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult_global(a, b, 7, 10) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult_global(a, b, 6, 10) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult_global(a, b, 5, 10) == [[2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult_global(a, b, 4, 10) == [[8, 20, 16, 4], [9, 11, 3],
                         [7, 7, 1], [12, 13, 3]]
assert mult_global(a, b, 3, 10) == [[9, 11, 3], [7, 7, 1], [12, 13, 3]]

assert mult_global(a, b, 3, 2) == [[9, 11, 3], [7, 7, 1], [12, 13, 3]]

assert mult_global(a, b, 3, 1) == [[11, 3], [7, 1], [13, 3]]


print('mult_global PASSED!\n')

print('ALL TESTS PASSED!')
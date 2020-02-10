# coding=utf8
from my_poly_functions import show_y, show, mult_y, mult, add_y, add


# тест функции show_y
assert show_y([2, 1, 3]) == '(2*y^2 + y^1 + 3)'
assert show_y([2, 0, 0]) == '(2*y^2)'
assert show_y([0, 3, 0]) == '(3*y^1)'
assert show_y([0, 0, 0]) == '()'
assert show_y([0]) == '()'
assert show_y([3]) == '(3)'
assert show_y([0, 0, 3]) == '(3)'
print('show_y PASSED!\n')

# тест функции show
assert show([[2, 1, 3], [0], [1, 2]]) == \
       '(2*y^2 + y^1 + 3)*x^2 + (y^1 + 2)'
print('show PASSED!\n')

# тест функции add_y
assert add_y([3, 5, 1, 4, 3], [2, 4, 2]) == [3, 5, 3, 8, 5]
assert add_y([2, 4, 2], [3, 5, 1, 4, 3]) == [3, 5, 3, 8, 5]
assert add_y([1, 4], [0]) == [1, 4]
print('add_y PASSED!\n')

# тест функции add
a = [[2,3,1], [2,1], [1,0], [3,1]]
b = [[0], [0], [0], [0], [1,1], [4,3]]
assert add(a, b) == [[0], [0], [2, 3, 1], [2, 1], [2, 1], [7, 4]]
print('add PASSED!\n')

# тест функции mult_y
a1 = [3, 2, 1]
b1 = [1, 1]
assert mult_y(a1, b1) == [3, 5, 3, 1]
print('mylt_y PASSED!\n')

# тест функции mult
a = [[2,3,1], [2,1], [1,0], [3,1]]
b = [[0], [0], [1,1], [4,3]]
assert mult(a, b) == [[0], [0], [2, 5, 4, 1], [8, 20, 16, 4], [9, 11, 3],
                      [7, 7, 1], [12, 13, 3]]
print('mult PASSED!\n')

print('ALL TEST PASSED!')
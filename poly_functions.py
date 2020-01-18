import numpy as np


def show_y(arr):
    step_y = len(arr)
    ans = "("
    for j in range(len(arr), 0, -1):
        if arr[j] != 0:
            if arr[j] != 1:
                ans += str(int(arr[j])) + '*' + 'y' + '^' + str(step_y) + ' + '
            else:
                ans += 'y' + '^' + str(step_y) + ' + '
        step_y -= 1
    if arr[0] != 0:
        ans += str(arr[0])
    elif ans != '(' and ans[-2] == '+':
        ans = ans[:-3]
    return ans + ')'


def show(arr):
    step_x = len(arr) - 1
    ans = ""
    for i in range(len(arr) - 1):
        if list(arr[i]) != [0] and show_y(arr[i]) != '()':
            ans += show_y(arr[i]) + '*' + 'x' +'^' + str(step_x) + ' + '
        step_x -= 1

    if list(arr[-1]) != [0] and show_y(arr[-1]) != '()':
        ans += show_y(arr[-1])
    elif ans and ans[-2] == '+':
        ans = ans[:-2]
    return ans


# реализуем перемножение двух многочленов от x, таких, что коэффициенты при x^i - это
# многочлены от y
def mult(a, b):
    ans = [np.poly1d([0])] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        # хотим вычислить коэффициент при x^((len(a) + len(b) - 1) - i)
        for j in range(len(b)):
            ans[i + j] += np.polymul(a[i], b[j])
    return ans

# реализуем сложение двух многочленов от x, таких, что коэффициенты при x^i - это
# многочлены от y
def add(a, b):
    if len(a) < len(b):
        a, b = b, a
    ans = a[::]
    ind = len(ans) - 1
    for i in range(len(b) - 1, -1, -1):
        ans[ind] = np.polyadd(ans[ind], b[i])
        ind -= 1
    return ans

def show_y(arr):
    step_y = len(arr) - 1
    ans = "("
    for j in range(len(arr) - 1):
        if arr[j] != 0:
            if arr[j] != 1:
                ans += str(arr[j]) + '*y^' + str(step_y) + ' + '
            else:
                ans += 'y^' + str(step_y) + ' + '
        step_y -= 1
    if arr[-1] != 0:
        ans += str(arr[-1])
    elif ans != '(' and ans[-2] == '+':
        ans = ans[:-3]
    return ans + ')'


def show(arr):
    step_x = len(arr) - 1
    ans = ""
    for i in range(len(arr) - 1):
        if list(arr[i]) != [0] and show_y(arr[i]) != '()':
            ans += show_y(arr[i]) + '*x^' + str(step_x) + ' + '
        step_x -= 1

    if list(arr[-1]) != [0] and show_y(arr[-1]) != '()':
        ans += show_y(arr[-1])
    elif ans and ans[-2] == '+':
        ans = ans[:-2]
    return ans


def add_y(a, b):
    if len(a) < len(b):
        a, b = b, a
    ans = a[::]
    ind = len(ans) - 1
    for i in range(len(b) - 1, -1, -1):
        ans[ind] += b[i]
        ind -= 1
    return ans


def add(a, b):
    if len(a) < len(b):
        a, b = b, a
    ans = a[::]
    ind = len(ans) - 1
    for i in range(len(b) - 1, -1, -1):
        ans[ind] = add_y(ans[ind], b[i])
        ind -= 1
    return ans


def mult_y(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        # хотим вычислить коэффициент при x^((len(a) + len(b) - 1) - i)
        for j in range(len(b)):
            ans[i + j] += a[i] * b[j]
    i = 0
    while i < len(ans) and ans[i] == 0:
        i += 1
    if i == len(ans):
        return [0]
    return ans[i:]


def mult(a, b):
    ans = [[0]] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        # хотим вычислить коэффициент при x^((len(a) + len(b) - 1) - i)
        for j in range(len(b)):
            ans[i + j] = add_y(ans[i + j], mult_y(a[i], b[j]))
    return ans


def make_equation(arr, xy_equation=True):
    a, b, c, d, series_size = arr
    x = [[1], [0]]
    y = [[1, 0]]
    minus_one = [[-1]]
    if (xy_equation):
        return mult(x,
                    add(mult(a, b),
                        mult(mult(add(y, minus_one),
                                  c),
                             d)))[-2 * series_size + 1:]
    else:
        return mult(x,
                    add(mult(a, b),
                        mult(mult(minus_one,
                                  c),
                             d)))[-2 * series_size + 1:]
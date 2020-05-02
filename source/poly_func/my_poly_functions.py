def show_local(arr: list, loc='y') -> list:
    step_y = len(arr) - 1
    ans = "("
    for j in range(len(arr) - 1):
        if arr[j] != 0:
            if arr[j] != 1:
                ans += str(arr[j]) + '*' + loc + '^' + str(step_y) + ' + '
            else:
                ans += loc + '^' + str(step_y) + ' + '
        step_y -= 1
    if arr[-1] != 0:
        ans += str(arr[-1])
    elif ans != '(' and ans[-2] == '+':
        ans = ans[:-3]
    return ans + ')'


def show_global(arr: list, glob='x', loc='y') -> list:
    step_x = len(arr) - 1
    ans = ""
    for i in range(len(arr) - 1):
        if arr[i] != [0] and show_local(arr[i], loc=loc) != '()':
            ans += show_local(arr[i], loc=loc) + '*' + glob +'^' + str(step_x) + ' + '
        step_x -= 1

    if list(arr[-1]) != [0] and show_local(arr[-1], loc=loc) != '()':
        ans += show_local(arr[-1], loc=loc)
    elif ans and ans[-2] == '+':
        ans = ans[:-2]
    return ans


def add_local(a: list, b: list) -> list:
    if len(a) < len(b):
        a, b = b, a
    ans = a[::]
    ind = len(ans) - 1
    for i in range(len(b) - 1, -1, -1):
        ans[ind] += b[i]
        ind -= 1
    i = 0
    while i < len(ans) and ans[i] == 0:
        i += 1
    if i == len(ans):
        return [0]
    return ans[i:]


def add_global(a: list, b: list) -> list:
    if len(a) < len(b):
        a, b = b, a
    ans = a[::]
    ind = len(ans) - 1
    for i in range(len(b) - 1, -1, -1):
        ans[ind] = add_local(ans[ind], b[i])
        ind -= 1
    return ans


def mult_local(a: list, b: list, max_pow) -> list:
    ans = [0] * min((len(a) + len(b) - 1), max_pow + 1)
    iterat_1 = min(len(a), max_pow + 1)
    ans_len = len(ans)
    a_len = len(a)
    b_len = len(b)
    for i in range(iterat_1):
        # хотим вычислить коэффициент при y^((len(a) + len(b) - 1) - i)
        iterat_2 = min(max_pow - i + 1, len(b))
        for j in range(iterat_2):
            ans[ans_len - i - j - 1] += a[a_len - i - 1] * b[b_len - j - 1]
    i = 0
    while i < ans_len and ans[i] == 0:
        i += 1
    if i == ans_len:
        return [0]
    return ans[i:]


def mult_global(a: list, b: list, x_size: int, y_pow: int) -> list:
    """
    вычисляет произведение двух мнгочленов от двух переменных
    :param a:
    :param b:
    :param size: размер по которому я 'обрезаю' многочлен.
                 Нужно для того, чтобы все степени многочлена
                 по х не превосходили заданного значение
                 (оно как раз и задаётся через size)
    :return:
    """
    ans = [[0]] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        # хотим вычислить коэффициент при x^((len(a) + len(b) - 1) - i)
        for j in range(len(b)):
            if (len(a) + len(b) - 1) - x_size <= i + j:
                ans[i + j] = add_local(ans[i + j], mult_local(a[i], b[j], y_pow))
    i = 0
    while i < len(ans) and ans[i] == [0]:
        i += 1
    if i == len(ans):
        return [[0]]
    ans = ans[i:]
    return ans[-x_size:]


def make_equation_cut(arr, xy_equation=True):
    a, b, c, d, x_size, y_pow = arr
    x = [[1], [0]]
    y = [[1, 0]]
    minus_one = [[-1]]
    if (xy_equation):
        return mult_global(x,
                           add_global(mult_global(a, b, 2 * x_size + 1, y_pow),
                                      mult_global(mult_global(add_global(y, minus_one),
                                                              c,
                                                              2 * x_size + 1,
                                                              y_pow),
                                           d,
                                           2 * x_size + 1,
                                           y_pow)),
                           2 * x_size + 1,
                           y_pow)[-2 * x_size + 1:]
    else:
        return mult_global(x,
                           add_global(mult_global(a, b, 2 * x_size + 1, y_pow),
                                      mult_global(mult_global(minus_one,
                                                       c,
                                                       2 * x_size + 1,
                                                       y_pow),
                                           d,
                                           2 * x_size + 1,
                                           y_pow)),
                           2 * x_size + 1,
                           y_pow)[-2 * x_size + 1:]


def mult_y(a: list, b: list) -> list:
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


def mult(a: list, b: list, size: int) -> list:
    """
    вычисляет произведение двух мнгочленов от двух переменных
    :param a:
    :param b:
    :param size: размер по которому я 'обрезаю' многочлен.
                 Нужно для того, чтобы все степени многочлена
                 по х не превосходили заданного значение
                 (оно как раз и задаётся через size)
    :return:
    """
    ans = [[0]] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        # хотим вычислить коэффициент при x^((len(a) + len(b) - 1) - i)
        for j in range(len(b)):
            if (len(a) + len(b) - 1) - size <= i + j:
                ans[i + j] = add_local(ans[i + j], mult_y(a[i], b[j]))
    i = 0
    while i < len(ans) and ans[i] == [0]:
        i += 1
    if i == len(ans):
        return [[0]]
    ans = ans[i:]
    return ans[-size:]


def make_equation(arr, xy_equation=True):
    a, b, c, d, series_size = arr
    x = [[1], [0]]
    y = [[1, 0]]
    minus_one = [[-1]]
    if (xy_equation):
        return mult(x,
                    add_global(mult(a, b, 2 * series_size + 1),
                        mult(mult(add_global(y, minus_one),
                                  c,
                                  2 * series_size + 1),
                             d,
                             2 * series_size + 1)),
                    2 * series_size + 1)[-2 * series_size + 1:]
    else:
        return mult(x,
                    add_global(mult(a, b, 2 * series_size + 1),
                        mult(mult(minus_one,
                                  c,
                                  2 * series_size + 1),
                             d,
                             2 * series_size + 1)),
                    2 * series_size + 1)[-2 * series_size + 1:]
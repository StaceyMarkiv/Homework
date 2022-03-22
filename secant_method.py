def func_1(x):
    result = 2 * ((x - 1) ** 2) - 1
    return result


def secant(x_0, x_1, function):
    x_2 = x1 - ((x_1 - x_0) / (function(x_1) - function(x_0))) * function(x_1)
    y_s = function(x_2)
    result = [x_2, y_s]
    return result


e = 0.0001
x_range = [[-10, -9.9], [10, 9.9]]
for xx in x_range:
    x0 = xx[0]
    x1 = xx[1]
    x2 = 0
    y = 1
    while True:
        if abs(y) < e:
            print('\ny < e')
            print('при x =', x2)
            break
        func_result = secant(x0, x1, func_1)
        x2 = func_result[0]
        y = func_result[1]
        # print(x2, ' - ', y)
        t = x1
        x1 = x2
        x0 = t

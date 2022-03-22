import numpy as np


def func_1(x):
    result = 2 * (x - 1) ** 2 - 1
    return result


def func_2(x):
    result = 1.2 * (x + 2) ** 3 + 2 * x
    return result


def func_3(x):
    result = np.sin(x) + np.cos(x) / (x ** (1 / 3)) - np.e ** x
    return result


def func_4(x):
    result = 1.4 * (x ** 4) + 1.5 * (x ** 3) - 3.2 * (x ** 2) + 1.6 * x - 4.1
    return result


def func_5(x, y):
    result = x ** 2 + y ** 2 - 2
    return result

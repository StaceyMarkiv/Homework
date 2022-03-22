import matplotlib.pyplot as plt
import math


def func_3_1(x):
    result = math.sin(x) + math.cos(x) / (x ** (1 / 3)) - math.e ** x
    return result


def float_range(start, stop, step):
    range_num = []
    if stop < start:
        print('Ошибка: stop < start')
    else:
        if start == stop:
            range_num.append(start)
            return range_num
        while start < stop:
            range_num.append(start)
            start += step
            if start >= stop:
                range_num.append(stop)
    return range_num


x3_1 = float_range(0.01, 2.5, 0.01)
y3_1 = []
for xx in x3_1:
    y3_1.append(func_3_1(xx))
fig3_1 = plt.figure()
graph3_1 = plt.plot(x3_1, y3_1)
plt.grid(True)
plt.show()

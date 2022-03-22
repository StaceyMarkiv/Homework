import random
import sys


def func_2(x):
    result = 1.2 * (x + 2) ** 3 + 2 * x
    return result


x0 = random.uniform(-10, 10)
x1 = random.uniform(-10, 10)
e = 0.0001
y0 = func_2(x0)
y1 = func_2(x1)
x2 = 0
y2 = 1
if abs(y0) < e:
    print('y0 < e')
    print('при x =', x0)
    sys.exit()
elif abs(y1) < e:
    print('y1 < e')
    print('при x =', x1)
    sys.exit()
else:
    while True:
        if abs(y2) < e:
            break
        x2 = x1 - ((x1 - x0)/(func_2(x1) - func_2(x0))) * func_2(x1)
        y2 = func_2(x2)
        print(x2, ' - ', y2)
        t = x1
        x1 = x2
        x0 = t
    print('\ny < e')
    print('при x =', x2)

import matplotlib.pyplot as plt
import numpy as np


def func_1(x):
    result = 2 * ((x - 1) ** 2) - 1
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


x1 = np.arange(-1, 4, 0.02)
y1 = func_1(x1)
fig1 = plt.figure()
plt.xlabel('ось x')
plt.ylabel('ось y')
graph1 = plt.plot(x1, y1)
plt.grid(True)
plt.show(block=False)

x2 = np.arange(-8, 2, 0.01)
y2 = func_2(x2)
fig2 = plt.figure()
plt.xlabel('ось x')
plt.ylabel('ось y')
graph2 = plt.plot(x2, y2)
plt.grid(True)
plt.show(block=False)

x3 = np.arange(0.01, 2.5, 0.01)
y3 = func_3(x3)
fig3 = plt.figure()
plt.xlabel('ось x')
plt.ylabel('ось y')
graph3 = plt.plot(x3, y3)
plt.grid(True)
plt.show(block=False)

x4 = np.arange(-2.8, 2, 0.01)
y4 = func_4(x4)
fig4 = plt.figure()
plt.xlabel('ось x')
plt.ylabel('ось y')
graph4 = plt.plot(x4, y4)
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


def func_5(x, y):
    result = x ** 2 + y ** 2 - 2
    return result


fig = plt.figure()
ax_3d = fig.add_subplot(projection='3d')
ax_3d.set_xlabel('ось x')
ax_3d.set_ylabel('ось y')
ax_3d.set_zlabel('ось z')
x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = func_5(xgrid, ygrid)
ax_3d.plot_wireframe(xgrid, ygrid, zgrid)
plt.grid(True)
plt.show()

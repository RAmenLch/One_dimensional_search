import matplotlib.pyplot as plt
import numpy as np


def f(x1):
    return 100*((x1+2-x1**2)**2) + (1-x1)**2
def a(x1,x2):
    return x1**2 + x2

x1 = np.arange(-5, 5, 0.1)


z = f(x1)

plt.figure()
plt.plot(x1, z, color = 'red', linewidth = 1, linestyle = '-')

# 设置坐标轴的取值范围
plt.xlim((-10, 10))
plt.ylim((0,1000))

# 设置坐标轴的lable
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()

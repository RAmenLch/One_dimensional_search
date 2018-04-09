from sympy import *



def f(x1,x2):
    return 100*((x2-x1**2)**2) + (1-x1)**2

init_printing(use_unicode=True)
x1,x2 = symbols("x1 x2")

fx = f(x1,x2)

a = diff(fx, x1)
b = diff(fx, x2)
print(a)
print(b)


'''
def f(x1,x2):
    return 100*((x2-x1**2)**2) + (1-x1)**2


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# 定义figure
fig = plt.figure()
# 将figure变为3d
ax = Axes3D(fig)

# 数据数目
n = 256
# 定义x, y
x = np.arange(-5, 5, 1)
y = np.arange(-5, 5, 1)

# 生成网格数据
X, Y = np.meshgrid(x, y)

# 计算每个点对的长度
#R = np.sqrt(X ** 2 + Y ** 2)
# 计算Z轴的高度
Z = f(X,Y)
print(Z)


plt.xlabel('X axis')
plt.ylabel('Y axis')

# 绘制3D曲面
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))

# 绘制从3D曲面到底部的投影
ax.contour(X, Y, Z, zdim = 'z', offset = -2, cmap = 'rainbow')

# 设置z轴的维度
ax.set_zlim(0, 100)

plt.show()
'''

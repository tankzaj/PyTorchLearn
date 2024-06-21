# 全网首次发布！2022B站最为通俗易懂的【机器学习-数学基础】教程，测试代码
# https://www.bilibili.com/video/BV1VA4y1d78D/?p=3&spm_id_from=pageDriver&vd_source=a40f70757b42c66c1b986721408adbc3

import numpy as np
# 乘积
a = np.array([1,2,3,4,5])
y = np.prod(a)

print(y)

# 随机数
r_dec = np.random.rand()
# 返回0到1之间的随机小数u
print(r_dec)


# 大量随机数均匀分布图
import matplotlib.pyplot as plt

n = 800  # 样本数
x = np.random.rand(n)
y = np.random.rand(n)

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x,y)
plt.title("大量随机数均匀分布图")
plt.grid()
plt.show()

# 使用正态分布的随机数
x = np.random.randn(n)
y = np.random.randn(n)
plt.scatter(x,y)
plt.title("使用正态分布的随机数")
plt.grid()
plt.show()

# 绘制二次函数
def my_func(t):
    return 3*t**2 + 2*t + 1
t = np.linspace(-3,3)
z = my_func(t)
plt.scatter(t,z)
plt.title("绘制二次函数")
plt.legend()
plt.show()

# sigmoid函数
# https://zhuanlan.zhihu.com/p/75588369?utm_id=0
import math
x = np.arange(-10, 10, 0.1)
y = []
for t in x:
    y_1 = 1 / (1 + math.exp(-t))
    y.append(y_1)
plt.plot(x, y, label="sigmoid")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(0, 1)
plt.legend()
plt.show()


# 梯度下降的实现，二次函数示例
def test_func(x):     # 计算最小值的函数
    return x**2 - 2*x
def grad_func(x):     # 导数
    return 2*x -2

eta = 0.1             # 学习系数
x = 4.0               # x初始值
record_x = []         # x的记录
record_y = []         # y的记录

for i in range(20):   # 将x更新20次
    y = test_func(x)
    record_x.append(x)
    record_y.append(y)
    x -= eta * grad_func(x)    # 梯度下降法公式

plt.scatter(record_x, record_y, label="绘制二次函数的梯度下降的实现")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
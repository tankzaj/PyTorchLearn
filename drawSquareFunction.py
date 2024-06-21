import matplotlib.pyplot as plt
import numpy as np

# 创建一个 x 轴的数据范围 GPT中文版回答的
x = np.linspace(-50, 50, 1000)  # 从 -5 到 5 生成100个点

# 定义二次函数的方程 y = ax^2 + bx + c
a = 1
b = -2
c = 1
y = a * x**2 + b * x + c

# 绘制图形
plt.plot(x, y, label='y = ax^2 + bx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function')
plt.grid(True)
plt.legend()
plt.show()

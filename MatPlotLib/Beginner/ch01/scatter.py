import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.random.rand(1000)

plt.scatter(x, y, c='b', label='Scatterd figure')
plt.legend(loc="upper center")
plt.show()
'''
legend的loc参数：文本标签位置
        best
        upper right
        upper left
        lower left
        lower right
        right
        center left
        center right
        lower center
        upper center
        center
'''

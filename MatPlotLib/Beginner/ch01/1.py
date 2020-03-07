import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.cos(x)
y2 = np.sin(x)
#print(x, "\n", y)

plt.plot(x, y1, ls="-", lw=5, label="Plot figure")
plt.scatter(x, y2, c='b', label='Scatterd figure')
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

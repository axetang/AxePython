import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.random.rand(1000)*10

plt.scatter(x, y, c='b', label='Scatterd figure')
plt.legend(loc="upper center")
plt.axhspan(ymin=2, ymax=4, xmin=0, xmax=10, facecolor="y", alpha=0.5)
#plt.axvspan(xmin=5, xmax=8, ymin=5, ymax=8, facecolor="r", alpha=0.1)
plt.axvspan(5, 8, 0, 8, facecolor="g", alpha=0.9)
plt.show()

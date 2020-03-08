import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.random.rand(1000)*10

plt.scatter(x, y, c='b', label='Scatterd figure')
plt.legend(loc="upper center")
plt.axhline(y=5, xmin=0, xmax=10, c="r", ls="--", lw=2)
plt.axvline(x=5, ymin=0, ymax=10, c="r", ls="--", lw=2)

plt.show()

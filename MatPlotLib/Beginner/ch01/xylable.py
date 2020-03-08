import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.random.rand(1000)*10

plt.scatter(x, y, c='b', label='Scatterd figure')
plt.legend(loc="upper center")
plt.xlim(0, 10)
plt.ylim(0, 5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

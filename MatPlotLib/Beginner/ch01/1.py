import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)
#print(x, "\n", y)

plt.plot(x, y, ls="-", lw=5, label="Plot figure by Axe Tang")
plt.scatter(x, z, c='b', label='scatterd figure')
plt.legend(loc="upper center")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.random.rand(1000)*10

plt.scatter(x, y, c='b', label='Scatterd figure')
plt.legend(loc="upper center")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(linestyle=":", color="r")
plt.text(5, 5, "text by axe", weight="bold", color='r')
plt.title("a scattered pic")
plt.show()

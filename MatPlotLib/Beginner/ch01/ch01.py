import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm as cm

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)
plt.scatter(x, y1, c="0.1", label="Scattered Figure")
plt.plot(x, y, ls="--", lw=2, label="Plot Figure")

# 清理上方和右方的框线，变成标准坐标轴
for spine in plt.gca().spines.keys():
    if spine == "top"or spine == "right":
        plt.gca().spines[spine].set_color("none")

plt.gca().xaxis.set_ticks_position("bottom")
plt.gca().yaxis.set_ticks_position("left")
#
plt.xlim(0.0, 4.0)
plt.ylim(-3, 3)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True, color='r', ls=":")
plt.axhline(y=0, c="r", ls="--", lw=2)

plt.axvspan(xmin=1.0, xmax=2.0, facecolor='y', alpha=0.3)
plt.annotate("Maximum", xy=(np.pi/2, 1.0),
             xytext=((np.pi/2)+0.15, 1.5), weight='bold', color='r',
             arrowprops=dict(
                 arrowstyle="->", connectionstyle="arc3", color='b'
))
plt.annotate("", (0, -2.78), xytext=(0.4, -2.32),
             arrowprops=dict(
                 arrowstyle="->", connectionstyle="arc3", color='b'
))
plt.annotate("", (3.5, -2.98), xytext=(3.6, -2.7),
             arrowprops=dict(
                 arrowstyle="->", connectionstyle="arc3", color='b'
))
plt.text(3.58, -2.7, "'|' is tickline", weight='bold', color='b')
plt.text(3.58, -2.95, "3.5 is ticklabel", weight='bold', color='b')
plt.title("Structure of Matplotlib")
plt.legend(loc="upper left")
plt.show()

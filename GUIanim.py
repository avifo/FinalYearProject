import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.gcf()
ax1 = fig.add_subplot(1, 1, 1)
# ax1.axes.get_xaxis().set_visible(False)
# ax1.axes.get_yaxis().set_visible(False)


# x is time
# y is data


# matplot ways of displaying data
def animate(i):
    graph_data = open("FileData.txt", "r").read()
    lines = graph_data.split('\n')
    xs = [0]
    ys = [0]
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xs.append(float(y))
            ys.append(float(x))

    ax1.clear()
    plt.ylim(-2, 6)
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=500)

plt.tight_layout()
plt.show()

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'


x_vals = []
y_vals = []

index = count()

plt.figure(figsize=(15, 5), dpi=60)


def animate(i):
    print('hello')
    curve = 100

    x = next(index)
    y = random.randint(300, 500)

    x_vals.append(x)
    y_vals.append(y)

    plt.cla()

    if x > curve:
        plt.plot(x_vals[-curve:], y_vals[-curve:], color="black")
        # plt.axis('off')
        plt.xticks([])
        plt.yticks([])
        x_vals.pop(0)
        y_vals.pop(0)
    else:
        plt.plot(x_vals, y_vals, color="black")
        plt.xticks([])
        plt.yticks([])


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()

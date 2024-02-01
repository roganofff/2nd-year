# движущийся график, который переходит из y = x в y = -x

from matplotlib import pyplot
import time

MAX = 100

x = y = list(range(MAX))

fig, ax = pyplot.subplots(1)
line, = ax.plot(x, y)

pyplot.ion()
pyplot.show()

running = True

def close(_):
    global running
    running = False

fig.canvas.mpl_connect('close_event', close)

step = 1
while running:
    if y[-1] == MAX - 1:
        step = -1
    elif y[-1] == 0:
        step = 1

    y.pop(0)
    y.append(y[-1] + step)

    line.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(0.01)

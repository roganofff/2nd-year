from matplotlib import pyplot
from psutil import cpu_percent, virtual_memory
import time

xs = [x for x in range(100)]
cpu, mem = [0 for _ in xs], [0 for _ in xs]

fig, ax = pyplot.subplots(2)
line_cpu = ax[0].plot(xs, cpu)
line_mem = ax[1].plot(xs, mem)
ax[0].set_ylim(0, 100)
ax[1].set_ylim(0, 100)

ax[0].title.set_text('CPU')
ax[1].title.set_text('MEMORY')

pyplot.ion()
pyplot.show()

running = True

def close(_):
    global running
    running = False

fig.canvas.mpl_connect('close_event', close)

def get_color(percent: int|float) -> str:
    if percent < 20:
        return 'green'
    elif percent < 40:
        return '#CFBF00'
    return 'red'        

while running:
    cpu.pop(0)
    mem.pop(0)
    cur_cpu, cur_mem = cpu_percent(), virtual_memory().percent
    cpu.append(cur_cpu)
    mem.append(cur_mem)
    line_cpu[0].set_ydata(cpu)
    line_mem[0].set_ydata(mem)

    line_cpu[0].set_color(get_color(sum(cpu[-10:]) / 10))
    line_mem[0].set_color(get_color(sum(mem[-10:]) / 10))

    fig.canvas.flush_events()
    fig.canvas.draw()

    time.sleep(.01)

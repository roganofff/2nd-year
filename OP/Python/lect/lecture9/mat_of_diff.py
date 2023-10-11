from matplotlib import pyplot
import math

x_sin = [x / 100 for x in range(1000)] # от 0 до 10
y_sin = [math.sin(x) for x in x_sin]

x_parabola = [x / 10 for x in range(-100, 101)] # от -10 до 10
y_parabola = [x ** 2 for x in x_parabola]

fig, axes = pyplot.subplots(2)

axes[0].plot(x_sin, y_sin, color='red', label='sin(x)')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].set_title('sin(x)')

axes[1].plot(x_parabola, y_parabola, color='black', label='x^2')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].set_title('parabolic function')

pyplot.show()


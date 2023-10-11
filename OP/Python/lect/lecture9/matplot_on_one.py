from matplotlib import pyplot

import math

# xs
xs = [x / 100 for x in range(1000)]

y_sin = [math.sin(x) for x in xs]
y_cos = [math.cos(x) for x in xs]

pyplot.plot(xs, y_sin, label='six(x)', color='blue')
pyplot.plot(xs, y_cos, label='cos(x)', color='red')
pyplot.legend()
pyplot.show()

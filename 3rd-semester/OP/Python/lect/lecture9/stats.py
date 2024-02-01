# столбцовые диаграммы
from matplotlib import pyplot

fig = pyplot.figure()

colors = {
    'pelmeni': '#EEEEEE',
    'borshtch': '#FF6600',
    'bread': '#964B00',
    'dorado': '#F5F5DC',
    'lemon water': '#FDF940',
    'buckwheat': '#BDB76B',
}

menu = [
    ('bread', 100.0),
    ('dorado', 72.0),
    ('lemon water', 50.0),
    ('borshtch', 80.0),
    ('pelmeni', 112.0),
    ('buckwheat', 400.0)
]
dishes = [dish[0] for dish in menu]
prices = [price[1] for price in menu]

bars = pyplot.bar(dishes, prices)

for index, dish in enumerate(dishes):
    bars[index].set_color(colors[dish])

pyplot.title('Menu prices')
pyplot.show()
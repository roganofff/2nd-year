from typing import Self


def checkers(attrs: tuple[str]):
    def checker(class_: type) -> type:
        def create_setter_getter(attr):
            def getter(self):
                return getattr(self, f'_{attr}')
            def setter(self, value):
                collection = getattr(self, f'_{attr}s')
                if not value in getattr(self, f'_{attr}s'):
                    raise ValueError(f'{value} not in {collection}')
                setattr(self, f'_{attr}', value) 
            return getter, setter
        for attr in attrs:
            getter, setter = create_setter_getter(attr)
            setattr(class_, attr, property(getter, setter))
        return class_
    return checker


class Flyweight:
    _pool = {}
    def __new__(cls, *args, **kwargs) -> Self:
        args_key = '_'.join([str(arg) for arg in args])
        kwargs_key = '_'.join([f'{key}-{value}' for key, value in kwargs.items()])
        key = args_key + kwargs_key
        if key in cls._pool.keys():
            return cls._pool[key]
        else:
            instance = super().__new__(cls)
            cls._pool[key] = instance
            return instance


@checkers(('width', 'color', 'length'))
class Leaf(Flyweight):
    _colors = 'red', 'green'
    _lengths = 'long', 'short'
    _widths = 'thin', 'wide'

    def __init__(self, width: str, length: str, color: str) -> None:
        self.width, self.length, self.color = width, length, color

    def __hash__(self) -> int:
        return hash(self.width, self.length, self.color)
for _ in range(10):
    Leaf('thin', 'long', 'green')
    
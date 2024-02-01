from typing import Callable


def ensure(attr: str, checker: Callable) -> Callable:
    def add_property(class_: type) -> type:
        def getter(self):
            return getattr(self, f'_{attr}')
        def setter(self, value):
            checker(value)
            setattr(self, f'_{attr}', value)
        setattr(class_, attr, property(getter, setter))
        return class_
    return add_property


def check_positive_int(value: int) -> None:
    if not isinstance(value, int):
        raise TypeError(f'Value is expected to be int, not {type(value).__name__}')
    if value < 0:
        raise ValueError(f'Value {value} is expected to be positive')


def check_name(name: str) -> None:
    if name.lower() == 'areg':
        raise ExceptionGroup(
            'у меня на это пять причин',
            [
                Exception('первая причина это ты'),
                Exception('а вторая все твои мечты'),
                ExceptionGroup(
                    'третья причина это я',
                    [
                        Exception('потому что слушаю тебя'),
                    ]
                ),
                Exception(4),
                Exception(5),
            ]
        )


@ensure('name', check_name)
@ensure('age', check_positive_int)
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

krdyan = Person('Areg', 20)
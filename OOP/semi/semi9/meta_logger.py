from typing import Any, Callable


def log_call(func: Callable, classname: str) -> Callable:
    def wrapped(*args, **kwargs):
        print(f'running {classname}.{func.__name__}')
        return func(*args, **kwargs)
    return wrapped


class MethodLogger(type):
    def __init__(cls, classname: str, _, attrs: dict[str, Any]) -> None:
        for attr, value in attrs.items():
            if callable(value):
                setattr(cls, attr, log_call(value, classname))

class Person(metaclass=MethodLogger):
    def walk(self):
        print('person is walking')

    def sleep(self):
        print('person is sleeping')

Person().walk()
Person().sleep()

from typing import Callable


def log_call(func: Callable, classname: str) -> Callable:
    def wrapped(*args, **kwargs):
        print(f'running {classname}.{func.__name__}')
        return func(*args, **kwargs)
    return wrapped


def log_method_calls(class_: type) -> type:
    for attr, value in class_.__dict__.items():
        if callable(value):
            setattr(class_, attr, log_call(value, class_.__name__))
    return class_

@log_method_calls
class Person:
    def walk(self):
        print('person is walking')

    def sleep(self):
        print('person is sleeping')

Person().walk()
Person().sleep()

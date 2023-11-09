from typing import Any, Callable

def log_name(func: Callable):
    def wrapped(*args, **kwargs) -> Callable:
        print(f'{func.__name__} was called')
        return func(*args, **kwargs)
    return wrapped

class Meta(type):
    def __new__(cls, name: str, bases: tuple[type], attrs: dict[str, Any]):
        for key, value in attrs.items():
            if callable(value):
                attrs[key] = log_name(value)
        return super().__new__(cls, name, bases, attrs)
    
class A(metaclass=Meta):
    def fst_method(self):
        print('hello world')

    def snd_method(self):
        print('goodbye, argun')

A().fst_method()
A().snd_method()
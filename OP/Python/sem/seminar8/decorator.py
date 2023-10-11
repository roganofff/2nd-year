# decorator wraps any function which return string and adds random cat
from typing import Callable
from random import choice
from generator import students_and_marks
from random import randint

def add_cat(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        cats = ['=(^-^)=', '-(^..^)-', '~($.$)~', '=(^w^)=']
        return f'{func(*args, **kwargs)} {choice(cats)}'
    return wrapper

@add_cat
def name():
    return 'Yehor Roganoff'

print(name())

import time

def log_start(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} started at {time.ctime()}')
        return func(*args, **kwargs)
    return wrapper

@log_start
def sum_two(first: int|float, second: int|float) -> int|float:
    """Sum the two numbers."""
    return first.__add__(second)

decorated_sum = log_start(sum_two)

print(sum_two.__doc__)
print(decorated_sum.__doc__)
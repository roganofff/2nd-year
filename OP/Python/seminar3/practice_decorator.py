from typing import Callable, Iterable, Generator
from time import sleep, monotonic
from random import randint


def get_time(func: Callable) -> Callable:
    def new(*args, **kwargs):
        start = monotonic()
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} выполнялась на протяжении {monotonic() - start}')
        return result
    return new

@get_time
def f(n: int) -> int:
    sleep(1)
    return n + 1

##############

def work_w_iterable(func: Callable) -> Callable:
    def new(source: str|Iterable) -> str:
        if isinstance(source, Iterable) and not isinstance(source, str):
            source = ' '.join(str(item) for item in source)
        return func(source)
    return new

@work_w_iterable
def calm_the_text(text: str) -> str:
    return text.lower().replace('!', '.')

# print(calm_the_text(['2.9.7.2', 'ВСЁ ЕЩЁ НЕ СДАЛИ', 'GITHUB!!!']))

#############

def square(func: Callable) -> Callable:
    return lambda *args: func(*args) ** 2

@square
def f(x):
    return x + 1

# print(f(1))

#############

from pprint import pprint

def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)  


def only_leap_years(func: Callable) -> Callable:
    def new(*args, **kwargs) -> list:
        dates = func(*args, **kwargs)
        return [date for date in dates if is_leap(date[2])]
    return new

@only_leap_years
def generate_birthdays(n: int) -> tuple:
    return [
        (
            randint(1, 28),
            randint(1, 12),
            randint(-6000, 2023),
        ) for _ in range(n)
    ]

# pprint(generate_birthdays(10))

#############

# декоратор генератора
def enum_generator(func: Callable) -> Callable:
    def new(*args, **kwargs) -> Generator:
        index = 0
        for value in func(*args, **kwargs):
            yield index, value
            index += 1
    return new


# генератор a.k.a. дегенератор
@enum_generator
def fibonacci(n: int) -> Generator:
    fst, snd = 0, 1
    yield fst

    while n > 1:
        yield snd
        fst, snd = snd, fst + snd
        n -= 1

# for ind, value in fibonacci(20):
#     print(f'Fibonacci #{ind}: {value}')

def round_(func: Callable) -> Callable:
    def new(*args, **kwargs) -> float:
        return round(func(*args, **kwargs), 2)
    return new
    

@round_
def divide(a: int|float, b: int|float) -> float:
    return a / b

print(10.22 / 3)
print(divide(10.22, 3))
# generator
from typing import Generator
from random import randint, choice
from string import ascii_lowercase

def gen_from_range(quantity: int, range_num: tuple[int, int] = (0, 10)) -> Generator:
    while quantity > 0:
        yield randint(*range_num)
        
        quantity -= 1


def students_and_marks(
        quantity: int,
        range_marks: tuple[int, int] = (2, 5),
        range_name_len: tuple[int, int] = (2, 10)
    ) -> Generator:
    while quantity > 0:
        name = ''.join([choice(ascii_lowercase) for _ in range(randint(*range_name_len))])
        yield name.capitalize(), randint(*range_marks)
        quantity -= 1

# for name, mark in students_and_marks(5):
#     print(name, mark)

from math import sqrt
from typing import List


def power_the_numbers(numbers: List[int]) -> List[int]:
    """Square even numbers in list, square root .

    Args:
        numbers: a source numbers list.

    Returns:
        list: even numbers squared, odd rooted.
    """
    for number in numbers:
        if not isinstance(number, int):
            raise Exception(f'numbers should be integers, not {type(number).__name__}')

    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number ** 2)
        else:
            result.append(sqrt(number))

    return result


if __name__ == '__main__':
    numbers = [num for num in range(-10, 11)] + ['5']
    print(numbers)
    print(power_the_numbers(numbers))

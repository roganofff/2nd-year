import pytest
from typing import List
from main import power_the_numbers

test_powers = (
    [1, 2, 9], [1.0, 4, 3.0],
    [25, 6, 81], [5.0, 36, 9.0],
)


@pytest.mark.parametrize('numbers, expected', test_powers)
def test_power_the_numbers(numbers: List[int], expected: List[int]):
    assert power_the_numbers(numbers) == expected


invalid_numbers = [1, 2, '3']

# 1
def test_invalid_numbers_1():
    with pytest.raises(Exception):
        power_the_numbers(invalid_numbers)


# 2
def test_invalid_numbers_2():
    pytest.raises(Exception, power_the_numbers, (invalid_numbers,))


# 3
@pytest.mark.slow()
@pytest.mark.xfail(raises=Exception)
def test_invalid_numbers_3():
    power_the_numbers(invalid_numbers)
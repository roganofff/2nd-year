import pytest
from typing import Tuple

from salary import hourly_salary, coach_salary


hourly_test_data = (
        ('junior', 160, (69600.0, 10400.0)),
        ('middle', 160, (104400.0, 15600.0)),
        ('senior', 160, (156600.0, 23400.0)),

        ('junior', 80, (52200.0, 7800.0)),
        ('middle', 80, (78300.0, 11700.0)),
        ('senior', 80, (117450.0, 17550.0)),
        
        ('junior', 11, (37192.50, 5557.50)),
        ('middle', 23, (59703.75, 8921.25)),
        ('senior', 37, (96406.88, 14405.62)),

        ('junior', 0, (34800.0, 5200.0)),
        ('middle', 0, (52200.0, 7800.0)),
        ('senior', 0, (78300.0, 11700.0)),
)

@pytest.mark.parametrize('position, hours, expected', hourly_test_data)
def test_hourly_salary(position: str, hours: float, expected: Tuple[float]):
    assert hourly_salary(position, hours) == expected


def test_failing_position():
    with pytest.raises(Exception): # тест выполнится положительно, если происходит ошибка
        hourly_salary('abcdef', 80)


groups_test_data = (
    ((15, 10, 11), (4698, 702)),
    ((22, 7, 2), (4045.5, 604.5)),
    ((0, 0, 0), (0, 0)),
    ([], (0, 0)),
    ((1, 1, 1), (391.5, 58.5))

)
@pytest.mark.parametrize('groups, expected', groups_test_data)
def test_coach_salary(groups: Tuple[int], expected: Tuple[float]):
    assert coach_salary(groups) == expected
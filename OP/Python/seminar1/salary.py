"""Module for calculating diffetent types of salaries."""

from typing import Tuple


TAX = 0.13


def after_tax(pretax: float) -> Tuple[float]:
    aftertax = round(pretax * (1 - TAX), 2)
    return aftertax, round(pretax - aftertax, 2)


def hourly_salary(position: str, hours: float) -> Tuple[float]:
    """Calculate houlry salary based on position in company and actual hours.

    Agrs:
        position: str - position in company,
        hours: float - actual hours.

    Returns:
        tuple of two floats - salary after tax and tax itself.

    Raises:
        Exception: if rate is not defined for position (position unknown).
    """
    # used consts
    rates = {
        'junior': 80000,
        'middle': 120000,
        'senior': 180000
    }
    normal_hours = 160

    # check if position is defined in rates
    rate = rates.get(position)
    if not rate:
        raise Exception(f'Position for position <{position}> is nor defined in company.')

    # calcilations
    half = rates[position] / 2
    pretax = round(half + half * (hours / normal_hours), 2)
    return after_tax(pretax)


def coach_salary(groups: Tuple[int]) -> Tuple[float]:
    """Calculate based on number of people in groups.
   
    Args:
        groups: Tuple[int] - number of people in each group

    Returns:
        tuple of two floats - salary after tax and tax itself.
    """
    rate = 150

    pretax = sum(groups) * rate
    return after_tax(pretax)



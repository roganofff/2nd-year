staff = {
     'Karateev': 1000,
     'Yeltsin': 10000,
     'Tsverkunov': 98,
     'Kuznetsova': 99,
     'Turin': 4123724,
     'Lee': 228133766,
     'Ng': 9999999999
}


def format_salary_(employee: tuple) -> str:
    """Format the salary info of employee.

    Args:
        employee: tuple of two - str and int.

    Returns:
        str: formated employee's salary.
    """
    return f'{employee[0]}: {employee[1]} руб.'


print(list(map(format_salary_, staff.items())))

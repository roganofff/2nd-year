"""Company with Departments of Employees, uses aggregation Employee -> Department -> Company."""
from typing import Any


def check(new_value: Any, classes: tuple[type[Any]] | type[Any]):
    """Check if new value is an instance of one of classes.

    Args:
        new_value (Any): _description_
        classes (tuple[type[Any]] | type[Any]): _description_

    Raises:
        TypeError: _description_
    """    
    if not isinstance(new_value, classes):
        value_class = type(new_value).__name__
        classnames = [cls_.__name__ for cls_ in classes] if isinstance(classes, tuple) else classes.__name__
        raise TypeError(f'{new_value} of {value_class} should be of {classnames}')


class Employee:
    """Employee of a company. Basic atomary class of company architecture."""
    def __init__(self, name: str, salary: float | int) -> None:
        """Name of an employee, positive numeric salary.

        Args:
            name (str): _description_
            salary (float | int): _description_
        """
        self.name, self.salary = name, salary

    @property
    def salary(self) -> float:
        """A salary of an employee.

        Returns:
            float: _description_
        """
        return self._salary

    @salary.setter
    def salary(self, new_salary: float | int) -> None:
        """Set a new positive numeric salary for an employee.

        Args:
            new_salary (float | int): _description_

        Raises:
            ValueError: _description_
        """
        check(new_salary, (int, float))
        if new_salary < 0:
            raise ValueError(f'salary {new_salary} is less than zero')
        self._salary = float(new_salary) if new_salary is int else new_salary


class Department:
    """A department of Company containing Employee instances if necessary."""

    def __init__(self, title: str, employees: list[Employee] | None = None) -> None:
        """Create a department with title and employees.

        Args:
            title (str): _description_
            employees (list[Employee] | None, optional): _description_. Defaults to None.
        """
        self.title = title
        self.employees = employees if employees is not None else []

    @property
    def salary(self) -> float:
        """Sum of salaries of all department employees.

        Returns:
            float: _description_
        """
        return sum(employee.salary for employee in self.employees)

    @property
    def employees(self) -> list[Employee]:
        """Get all employees of a department.

        Returns:
            list[Employee]: _description_
        """
        return self._employees
    
    @employees.setter
    def employees(self, new_employees: list[Employee]) -> None:
        """Set new employees list for department.

        Args:
            new_employees (list[Employee]): _description_
        """
        check(new_employees, list)
        for employee in new_employees:
            check(employee, Employee)
        self._employees = new_employees


class Company:
    """A company than aggregates Departments of Employees."""

    def __init__(self, title: str, departments: list[Department] | None = None) -> None:
        """Create a department with title and departments list if necessary.

        Args:
            title (str): _description_
            departments (list[Department] | None, optional): _description_. Defaults to None.
        """
        self.title = title
        self.departments = departments if departments is not None else []

    @property
    def employees(self) -> list[Employee]:
        """All employees of all departments of a company.

        Returns:
            list[Employee]: _description_
        """
        return list({[employee for dept in self.departments for employee in dept.employees]})

    @property
    def departments(self) -> list[Employee]:
        """Get all departments of a company.

        Returns:
            list[Employee]: _description_
        """
        return self._departments

    @departments.setter
    def departments(self, new_departments: list[Department]) -> None:
        """Set new department list for.

        Args:
            new_departments (list[Department]): _description_
        """
        check(new_departments, list)
        for department in new_departments:
            check(department, Department)
        self._departments = new_departments

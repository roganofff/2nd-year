from abc import ABC, abstractmethod
from typing import Iterable


class Sort(ABC):
    @staticmethod
    @abstractmethod
    def sort(items: Iterable, reverse: bool = False, **kwargs) -> Iterable:
        pass

class Default(Sort):
    @staticmethod
    def sort(items: Iterable, reverse: bool = False) -> Iterable:
        return sorted(items, reverse=reverse)
    
class ByParameter(Sort):
    @staticmethod
    def sort(items: Iterable, parameter: str, reverse: bool = False) -> Iterable:
        return sorted(items, key=lambda item: getattr(item, parameter), reverse=reverse)

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} {self.age}'

numbers = [1, 4, 9, 3]
people = [Person('Ivan', 20), Person('Petr', 30), Person('Pavel', 25)]
print(*Default.sort(numbers))
print(*ByParameter.sort(people, parameter='age'))
from typing import Self
from random import randint

class InvalidMarkError(Exception):
    def __init__(self, mark: int) -> None:
        super().__init__(f'mark cannot be {mark}')

class Student:
    __marks_range = 0, 5

    def __init__(self, name: str, marks: list[int]) -> None:
        self.name, self.marks = name, marks

    @property
    def marks(self) -> list[int]:
        return self.__marks
    
    @marks.setter
    def marks(self, new_marks: list[int]) -> None:
        if not isinstance(new_marks, (list, tuple)):
            raise TypeError('marks should be list or tuple')
        for mark in new_marks:
            if not isinstance(mark, int):
                raise TypeError(f'mark should be int, not {type(mark).__name__}')
            lower, upper = self.__class__.__marks_range
            if mark < lower or mark > upper:
                raise InvalidMarkError(mark)
        self.__marks = new_marks

    @property
    def average_score(self) -> float:
        return round(sum(self.marks) / len(self.marks), 2) if self.marks else 0.
    
    def __gt__(self, other: Self) -> bool:
        return self.average_score > other.average_score
    
    def __lt__(self, other: Self) -> bool:
        return self.average_score < other.average_score
    
    def __ge__(self, other: Self) -> bool:
        return self.average_score >= other.average_score
    
    def __le__(self, other: Self) -> bool:
        return self.average_score <= other.average_score
    
    def __eq__(self, other: Self) -> bool:
        return self.average_score == other.average_score
    
    def __ne__(self, other: Self) -> bool:
        return self.average_score != other.average_score
    
    def __str__(self) -> str:
        return f'{self.name} {self.average_score}'
    
names = (
    'Цверкунов Богдан',
    'Роганов Егор',
    'Каратеев Александр',
    'Владислав Безносов',
         )
students = [Student(name, [randint(0,4) for _ in range(0, 10)]) for name in names]

for student in students:
    if randint(0, 99) < 9:
        student.marks += [5]

print(*students, sep='\n')
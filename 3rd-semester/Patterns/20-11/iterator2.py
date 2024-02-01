from random import randint
from typing import Generator, Self


class Student:
    def __init__(self, name: str, avg_score: float) -> None:
        self.name = name
        self.avg_score = avg_score

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} avg_score={self.avg_score}'
    
class Group:
    def __init__(self, title: str, students: list[Student]) -> None:
        self.title = title
        self.students = students.copy()
        self._iterator = students.copy()

    @property
    def avg_score(self) -> float:
        return sum(student.avg_score for student in self.students) / len(self.students)
    
    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> Student:
        if not self._iterator:
            self._iterator = self.students.copy()
            raise StopIteration
        return self._iterator.pop(0)


class Teacher:
    def __init__(self, name: str, score_range: tuple[int, int]) -> None:
        self.name, self._score_range = name, score_range

    def __iter__(self) -> Generator:
        """Be careful, this generator is infinite."""
        def generate_score():
            while True:
                yield randint(*self._score_range)
        return generate_score()        

    
litvinov, vavilov = Student('Litvinov', 5.0), Student('Vavilov', 3.4)
group_9_2_8 = Group('normal\'nye rebyata', [litvinov, vavilov])
gomzyakov = Teacher('Boris Igorevich', (2, 5))
for student, score in zip(group_9_2_8, gomzyakov):
    print(f'{student} has got {score}')

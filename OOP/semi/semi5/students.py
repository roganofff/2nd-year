# метод записи множества студентов в файл json
# метод записи объекта студента в файл json, создание объекта стундета из файла json
# метод записи объекта студента в json, создание объекта стундета из json
# метод записи студента в словарь, создание студента из словаря

from typing import Self, Optional
from random import randint
import json


class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} {self.age} y.o.'

    def to_dict(self) -> dict:
        return self.__dict__
    
    @classmethod
    def from_dict(cls, attrs: dict) -> Self:
        return cls(**attrs)
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls(**json.loads(json_str))
    
    def to_json_file(self, filename: Optional[str] = None) -> None:
        filename = filename if filename else f'{self.name}.json'
        with open(filename, 'w') as new_json:
            json.dump(self.to_dict(), fp=new_json, indent=4)

    @classmethod
    def from_json_file(cls, filename: str) -> None:
        with open(filename, 'r') as json_file:
            return cls.from_dict(json.load(json_file))

    @staticmethod
    def set_to_json_file(students: list[Self], filename: str) -> None:
        all_students = {student.name: student.to_dict() for student in students}
        with open(filename, 'w') as new_json:
            json.dump(all_students, fp=new_json, ensure_ascii=False)

names = (
    'Цверкунов Богдан',
    'Роганов Егор',
    'Каратеев Александр',
    'Владислав Безносов',
)
students = [Student(name, randint(14, 20)) for name in names]
Student.set_to_json_file(students, 'K0709-22_2.json')
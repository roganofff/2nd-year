from abc import ABC
import random

class TalkingMixin(ABC):
    _standard_phrase: str
    def say(self, phrase: str = None) -> None:
        print(f'{self.name}: {phrase}' if phrase is not None else self._standard_phrase)

class Person(TalkingMixin):
    _standard_phrase = 'I live to see man-made horrors beyond my comprehension.'

    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    def live(self) -> None:
        print(f'{self.name} suffers.')

class Student(Person):
    __point_prob = 30
    _standard_phrase = 'I live to come up man-made horrors beyond my comprehension.'


    def __init__(self, name: str, age: int, group: str) -> None:
        super().__init__(name, age)
        self.group = group

    def get_oop_test_mark(self) -> float:
        mark = .0
        for _ in range(5):
            if random.randint(0, 99) < self.__point_prob:
                mark += 1.0
        if random.randint(0, 99) < self.__point_prob:
            mark -= .5

        return mark if mark > 0 else .0
    
class Cat(TalkingMixin):
    _standard_phrase = 'meow.'

    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

komarov = Student('Artyom', -5, 'K0711-23')
tereshin = Person('Slavik', -6)
vezdeskok = Cat('Murzik', 2)

for instance in (komarov, tereshin, vezdeskok):
    instance.say()
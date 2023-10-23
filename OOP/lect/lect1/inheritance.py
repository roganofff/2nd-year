
from oop import show_method

class Person: # Parent class (класс-предок)
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    def speak(self, text: str) -> None:
        print(f'{self.name}: {text}')

class Student(Person): # Child class (класс-потомок)
    def __init__(self, name: str, age: int, group: str) -> None: # method override
        super().__init__(name, age)
        self.group = group

    def speak(self, text: str) -> None:
        print(f'I am a student')
        super().speak(text)

    def __del__(self): # desctructor method
        show_method(self.__class__.__name__, 'Deleting', name=self.name)
        del self

class Teacher(Person):
    sleep = None
    def __init__(self, name: str, age: int, work: str) -> None:
        super().__init__(name, age)
        self.work = work

    def speak(self, text: str) -> None:
        print(f'{self.__class__.__name__} (works at {self.work})')
        super().speak(text)

# фу так делать
# def change_class(obj, target: type) -> None:
#     obj.__class__ = target
#     print('object type:', type(obj))
#     print('object class:', (obj.__class__))

argun = Student('Argun', 36, 'K0709-22/1')
zga = Teacher('Zernov Gleb Aleksandrovich', 60, 'IT-College Sirius')
argun.speak('ДА МНЕ НЕ 36!!!')
# argun.guitar = 'Шестиструнная' тоже хуйня
# print(argun.guitar)
zga.speak('Открываем пайтон юпитер')

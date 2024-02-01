def decorator(method):
    def wrapper(*args, **kwargs):
        print('Славик, выйди.')
        return method(*args, **kwargs)
    return wrapper

class MetaSlavik(type):
    def __new__(cls, name: str, bases: tuple, attrs: dict):
        for attr, value in attrs.items():
            if callable(value):
                attrs[attr] = decorator(value)
        return super().__new__(cls, name, bases, attrs)
    
class Student(metaclass=MetaSlavik):
    def attend_lesson(self) -> None:
        print('Я иду на пару.')

    def go_home(self):
        print('Ja domoi.')

vadim = Student()
vadim.attend_lesson()
vadim.go_home()
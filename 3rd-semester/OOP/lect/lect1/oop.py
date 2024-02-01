from time import sleep

def show_method(classname: str, action: str, **kwargs):
    print(f'{action} object of {classname}: {kwargs}')

class Student(object): # type
    is_lazy: bool = True

    def __new__(cls, name): # метод конструктор, который создаёт объект в памяти.
        show_method(cls.__name__, 'Creating', name=name)
        return super().__new__(cls)

    def __init__(self, name) -> None: # magic method (dunder method)
        self.name = name
        # self - ключевое слово, которое указывает на сам объект
        if name == 'Zaitsev':
            self.is_lazy = False
        show_method(self.__class__.__name__, 'Initializing', name=name)

    def __del__(self): # desctructor method
        show_method(self.__class__.__name__, 'Deleting', name=self.name)
        del self

    def greet(self): # object method
        print(f'Hello, I am {self.__class__.__name__} my name is {self.name}')

# Alexey = Student('Zaitsev')
# print(Alexey.name, Alexey.is_lazy)

# Atryom = Student('Nehoroshev')
# print(Atryom.name, Atryom.is_lazy)

# # Atryom.greet()
# Student.greet(Atryom)

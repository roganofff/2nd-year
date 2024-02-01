from abc import ABC, abstractmethod


class Animal(ABC):
    tail = horns = hoofs = wings = fur = False

    @abstractmethod
    def __init__(self, age: int) -> None:
        self.age = age

    def __str__(self) -> str:
        attrs = ['tail', 'horns', 'hoofs', 'wings', 'fur']
        # attrs = [attr for attr in attrs if getattr(self, attr)] same shii
        attrs = ', '.join(list(filter(lambda attr: getattr(self, attr), attrs)))

        return f'{self.__class__.__name__} with {attrs}'

class Tailed(Animal):
    tail = True
        
class Hoofed(Animal):
    hoofs = True
        
class Horned(Animal):
    horns = True
        
class Winged(Animal):
    wings = True
        
class Furry(Animal):
    fur = True

class Cat(Tailed, Furry, Horned):
    def __init__(self, age: int) -> None:
        super().__init__(age)

print(Cat(10))
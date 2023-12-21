class Unit:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        print(f'{self.__class__.__name__} {self.name}')

    def attack(self, other_unit):
        print(f'{self} attacks {other_unit}')

a = Unit('jopa')
b = Unit('Mocha')
a.attack(b)
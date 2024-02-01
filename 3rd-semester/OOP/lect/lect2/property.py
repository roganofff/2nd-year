class InvalidAge(ValueError):
    pass


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        if new_age < 0:
            raise InvalidAge(f'Age {new_age} is less than zero.')
        self.__age = new_age

noskov = Person('Misha', 54)
print(noskov.age())
noskov.age(11)
print(noskov.age())

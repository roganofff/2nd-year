# Composite pattern


from abc import ABC, abstractmethod
from random import choice, randint
from typing import Any, Self


class Product:
    def __init__(self, name: str, storage_temp: int) -> None:
        self.name, self.storage_temp = name, storage_temp

    def __str__(self) -> str:
        return f'Product {self.name}, {self.storage_temp}'



def check(new_value: Any, classes: tuple[type[Any]] | type[Any]):
    if not isinstance(new_value, classes):
        value_class = type(new_value).__name__
        classnames = [cls_.__name__ for cls_ in classes] if isinstance(classes, tuple) else classes.__name__
        raise TypeError(f'{new_value} of {value_class} should be of {classnames}')


class Fridge:
    def __init__(
            self,
            fridge: list[Product],
            freezer: list[Product],
            freezer_temp_range: tuple[int, int],
            fridge_temp_range: tuple[int, int],
        ) -> None:
        self.fridge, self.freezer = fridge, freezer
        self.freezer_temp_range = freezer_temp_range if freezer_temp_range is not None else []
        self.fridge_temp_range = fridge_temp_range if fridge_temp_range is not None else []

    @property
    def freezer(self) -> list[Product]:
        return self._freezer
    
    @freezer.setter
    def freezer(self, products: list[Product]):
        check(products, list)
        for product in products:
            check(product, Product)
        self._freezer = products

    @property
    def fridge(self) -> list[Product]:
        return self._fridge
    
    @fridge.setter
    def fridge(self, products: list[Product]):
        check(products, list)
        for product in products:
            check(product, Product)
        self._fridge = products

    @property
    def products(self) -> list[Product]:
        return self._freezer + self._fridge

    def __str__(self) -> str:
        return f'Warehouse {[str(product) for product in self._products]}'
    
    def add(self, product: Product) -> None:
        check(product, Product)
        if self.fridge_temp_range[0] <= product.storage_temp <= self.fridge_temp_range[1]:
            self._fridge.append(product)
        elif self.freezer_temp_range[0] <= product.storage_temp <= self.freezer_temp_range[1]:
            self._freezer.append(product)
        else:
            raise ValueError(f'Product {product} cannot be stored in fridge or freezer')

    def remove(self, product: Product) -> None:
        check(product, Product)
        if product in self._freezer:
            self._freezer.remove(product)
        elif product in self._fridge:
            self._fridge.remove(product)
        else:
            raise ValueError(f'There is no {product} in the fridge or freezer')

    def get(self, name: str) -> list[str]:
        return list(map(str, filter(lambda product: name.lower() in product.name, self.products)))
    

jablko = Product('Jabłko', 10)
fridge = Fridge([jablko, Product('Myaso iz kirpich', 5)], [Product('Morozhenoe', 0)], (-8, 8), (7, 14))
print(*fridge.products)
fridge.add(Product('Kiprich', 0))
print(*fridge.products)
fridge.remove(jablko)
print(fridge.get('kirpich'))


#######################################
# Builder pattern


class Vehicle(ABC):
    def move(self) -> None:
        print(f'{self.__class__.__name__} is riding on a {self.surface} at speed {self.speed}')

    def set_surface(self, surface: str) -> Self:
        self.surface = surface
        return self
    
    def set_speed(self, speed: int) -> Self:
        self.speed = speed
        return self
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass
    

class VehicleCreator(ABC):
    _surface: str
    _speed: int

    @classmethod
    @abstractmethod
    def create(cls) -> Vehicle:
        pass

class BoatCreator(VehicleCreator):
    _surface = 'Water'

    def create(cls, speed: int) -> Vehicle:
        return (Boat().set_surface(cls._surface).set_speed(speed))

class CarCreator(VehicleCreator):
    _surface = 'Asphalt'

    def create(cls, speed: int) -> Vehicle:
        return (Car().set_surface(cls._surface).set_speed(speed))

BoatCreator().create(60).move()
CarCreator().create(90).move()


############################
# Singleton pattern


class Singleton:
    _instance = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class PersonAttrsCreator(Singleton):
    _ages: list = list(range(0, 100))
    _alphabet: str = 'abcdefghijklmnoprstuvwxyz'

    @classmethod
    def age(cls) -> int:
        return cls._ages.pop(randint(0, len(cls._ages) - 1))

    @classmethod
    def name(cls) -> str:
        return ''.join(choice(cls._alphabet) for _ in range(randint(0, 20))).title()

for _ in range(101):
    print(PersonAttrsCreator().age())
    print(PersonAttrsCreator().name())
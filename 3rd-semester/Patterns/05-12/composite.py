from datetime import date
from typing import Any


def check(new_value: Any, classes: tuple[type[Any]] | type[Any]):
    if not isinstance(new_value, classes):
        value_class = type(new_value).__name__
        classnames = [cls_.__name__ for cls_ in classes] if isinstance(classes, tuple) else classes.__name__
        raise TypeError(f'{new_value} of {value_class} should be of {classnames}')


class Product:
    def __init__(self, name: str, expires: date) -> None:
        self.name, self.expires = name, expires

    @property
    def expires(self) -> date:
        return self._expires
    
    @expires.setter
    def expires(self, new_date: date) -> None:
        check(new_date, date)
        self._expires = new_date

    def __str__(self) -> str:
        return f'Product {self.name}, {self.expires}'


class Warehouse:
    def __init__(self, products: list[Product] | None = None) -> None:
        self.products = products if products is not None else []

    @property
    def products(self) -> list[Product]:
        return self._products
    
    @products.setter
    def products(self, new_products: list[Product]) -> None:
        check(new_products, list)
        for product in new_products:
            check(product, Product)
        self._products = new_products

    def __str__(self) -> str:
        return f'Warehouse {[str(product) for product in self._products]}'
    
    def add(self, product: Product) -> None:
        check(product, Product)
        self._products.append(product)

    def remove(self, product: Product) -> None:
        if product not in self._products:
            raise ValueError(f'{product} item is not present in product list')
        self._products.remove(product)

    def clean(self) -> None:
        self._products = list(filter(lambda product: product.expires >= date.today(), self._products))

warehouse = Warehouse([Product('Jabłko', date(2023, 11, 4)), Product('Ciasteczka', date(2023, 12, 5))])
prod = Product('Mięso', date(2023, 12, 5))
warehouse.add(prod)
print(warehouse)
warehouse.remove(prod)
warehouse.clean()
print(warehouse)
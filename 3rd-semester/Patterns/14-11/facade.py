# Facade 

from typing import Callable


class AdsGetter:
    def __init__(self, ads: list[str]) -> None:
        self._ads = ads

    def get(self) -> str:
        ad = self._ads.pop(0)
        self._ads.append(ad)
        return ad

    def add(self, ad: str) -> None:
        if not isinstance(ad, str):
            raise TypeError(f'AdsGetter expects ad to be str, not {type(ad).__name__}')
        self._ads.append(ad)

    def remove(self, ad: str) -> None:
        if ad not in self._ads:
            raise ValueError(f'Ad {ad} is not in AdsGetter ads list.')
        while ad in self._ads:
            self._ads.remove(ad)

class Size: # нужны property width, height, __str__, properties use positive in validation
    def __init__(self, width: int, height: int) -> None:
        self.width, self.height = width, height

    def check_positive_int(func: Callable) -> Callable:
        def wrapper(self, value: int):
            if not isinstance(value, int):
                raise TypeError(f'Value must be int, not {type(value).__name__}')
            if value < 0:
                raise ValueError('Value must be positive')
            return func(self, value)
        return wrapper

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    @check_positive_int
    def width(self, new_width: int) -> None:
        self._width = new_width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    @check_positive_int
    def height(self, new_height: int) -> None:
        self._height = new_height

    def __str__(self) -> str:
        return f'Size of ad: {self.width}x{self.height}'

class Billboard():
    def __init__(self, ads_getter: AdsGetter, size: Size) -> None:
        self.ads_getter, self.size = ads_getter, size

    def show(self) -> None:
        print(f'{self.ads_getter.get()} sized {self.size}')

ads = AdsGetter(['Sirius', 'MIPT', 'Albert Andreevich', 'Vyacheslav Aleksandrovich'])
bb = Billboard(ads, Size(1920, 1080))
while True:
    input()
    bb.show()
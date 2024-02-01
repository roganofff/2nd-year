import math

class Circle:
    def __init__(self, radius: int|float, ):
        self.radius = radius

    @property
    def radius(self) -> int|float:
        return self._radius
    
    @radius.setter
    def radius(self, new_radius: int|float) -> None:
        if not isinstance(new_radius, (int, float)):
            raise TypeError(f'{type(new_radius).__name__} is not int or float')
        if new_radius < 0:
            raise ValueError(f'{new_radius} < 0')
        self._radius = new_radius

    def length(self):
        return round(math.pi * self.radius * 2, 2)

    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    

cir = Circle(6)
print(cir.length(), cir.area())
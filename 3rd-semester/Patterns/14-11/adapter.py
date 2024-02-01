# pattern Adapter
# Adatpee -/-> Target
# Adaptee -> Adapter -> Target
# Size -> feet, inches
# Person -> name, height (cm)
# ImperialToCm

class Size:
    def __init__(self, feet: int, inches: int) -> None:
        self.feet, self.inches = feet, inches

    def to_typle(self) -> tuple[int, int]:
        return self.feet, self.inches

class ImperialToCentimeters:
    _feet_inches = 12
    _inch_cms = 2.54

    @classmethod
    def process(cls, value):
        if isinstance(value, Size):
            return (value.feet * cls._feet_inches + value.inches) * cls._inch_cms
        if isinstance(value, (int, float)):
            return value
        raise TypeError(f'Size must be int | float | Size, not {type(value).__name__}')

class Person:
    def __init__(self, name: str, height: float) -> None:
        """Height in centimeters."""
        self.name, self.height = name, height

Person('Krdyan', 191)
tyurin = Person('Tyurin', ImperialToCentimeters.process(Size(5, 10)))
print(tyurin.height)
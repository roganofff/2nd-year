from typing import Self

class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return f'{self.__class__.__name__} x={self.x}, y={self.y}'

    def __gt__(self, other: Self) -> bool:
        return self.x > other.x and self.y > other.y

    def __lt__(self, other: Self) -> bool:
        return self.x < other.x and self.y < other.y
    
    def __ge__(self, other: Self) -> bool:
        x_eq = self.x == other.x and self.y > other.y
        y_eq = self.y == other.x and self.y > other.y
        return x_eq or y_eq
    
    def __le__(self, other: Self) -> bool:
        x_eq = self.x == other.x and self.y < other.y
        y_eq = self.y == other.x and self.y < other.y
        return x_eq or y_eq
    
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other: Self) -> bool:
        return not self == other
    
    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y)

print(Point(1, 2) - Point(2, 3) + Point(10, 12) - Point(7, 3))

# points = [Point(x, y) for x, y in ((1,1), (1,2), (2,1), (2,2))]
# for point in points:
#     for other in points:
#         print(f'{point} < {other}: {point < other}')
#         print(f'{point} <= {other}: {point <= other}')
#         print(f'{point} > {other}: {point > other}')
#         print(f'{point} >= {other}: {point >= other}')
#         print(f'{point} == {other}: {point == other}')
#         print(f'{point} != {other}: {point != other}')
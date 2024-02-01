from typing import Self


class Flyweight:
    _pool = {}
    def __new__(cls, color, radius) -> Self:
        key = hash(color, radius)
        if key not in cls._pool.keys():
            cls._pool[key] = super().__new__(cls)
        return cls._pool[key]


class Ball(Flyweight):
    def __init__(self, color: str, radius: float) -> None:
        self.color, self.radius = color, radius

    def __hash__(self, color: str, radius: float) -> int:
        return hash(color, radius)


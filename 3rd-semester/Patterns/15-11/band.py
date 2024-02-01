# Facade

from abc import ABC
from typing import Self


class Musician(ABC):
    def __new__(cls, *args, **kwargs) -> Self:
        if cls is Musician:
            raise TypeError('Cannot instantiate object from abstract Musician class.')
        return super().__new__(cls)

    def __init__(self, name: str) -> None:
        self.name = name

    def play(self, piece: str) -> None:
        print(f'{self.__class__.__name__} {self.name}: {piece}')

class Guitarist(Musician):
    pass

class Vocalist(Musician):
    pass

class Drummer(Musician):
    pass

class Song:
    def __init__(self, parts: list[str, str]) -> None:
        self.parts = parts

class Band:
    def __init__(self, musicians: list[Musician], songs: list[Song]) -> None:
        self._musicians, self._songs = musicians, songs
    
    def perform(self) -> None:
        for song in self._songs:
            for part in song.parts:
                for role, piece in part.items():
                    for musician in self._musicians:
                        if musician.__class__.__name__ == role:
                            musician.play(piece)

hello = Song(
    [
        {
            'Guitarist': 'piano dolce', 
            'Vocalist':  'Hello, it\'s me',
        },
        {
            'Guitarist': 'mezzo forte',
            'Vocalist': 'Hello from the other siiiiiiiide',
            'Drummer': 'tam tam tam ts tum',
        }
    ]
)

roganov = Vocalist('Roganov')
demyanenko = Guitarist('SlavicYD')
zakhar = Drummer('Startsew')
Band([roganov, demyanenko, zakhar], [hello]).perform()
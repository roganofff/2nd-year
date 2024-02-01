from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    def __lt__(self, other) -> bool:
        return self.age < other.age
    
    def __gt__(self, other) -> bool:
        return self.age > other.age
    
    def __ge__(self, other) -> bool:
        return self.age >= other.age
    
    def __le__(self, other) -> bool:
        return self.age <= other.age
    
    def __eq__(self, other) -> bool:
        return self.age == other.age
    
    def __lt__(self, other) -> bool:
        return not self.age.__eq__(other.age)

    def __str__(self) -> str:
        return f'{self.__class__.__name__} name={self.name} age={self.age}'
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError(f'Player\'s age should be int.')
        limits = self.age_limit
        if limits and not limits[0] <= new_age <= limits[1]:
            raise ValueError(f'{self.__class__.__name__}\'s age should be from {limits[0]} to {limits[1]}.')
        self._age = new_age

    @classmethod
    def from_dict(cls, desc: dict):
        return cls(desc['name'], desc['age'])
    
    @classmethod
    def from_string(cls, desc: str):
        desc_list = desc.split(' ')
        try:
            int(desc_list[1])
        except ValueError as err:
            raise err
        return cls(desc_list[0], int(desc_list[1]))
    
    @staticmethod
    def many_to_dict(*players) -> list[tuple]:
        result = []
        for player in players:
            result.append((player.__class__.__name__, (player.name, player.age)))
        return result

class SchoolLeaguePlayer(Player):
    age_limit: tuple[int, int] = (14, 18,)

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)


vas = SchoolLeaguePlayer('vasya', 16)
pet = SchoolLeaguePlayer('petya', 18)
print(vas > pet, vas != pet)
vas.age = 19
print(vas)
print(pet.age)
kat = SchoolLeaguePlayer.from_string('Katya 16')
kat.age = 15
print(kat)
print(SchoolLeaguePlayer.many_to_dict(kat, vas, pet))
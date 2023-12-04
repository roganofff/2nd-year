from abc import ABC, abstractmethod


class InvalidWeaponType(Exception):
    def __init__(self, weapon_type: str) -> None:
        super().__init__(f'Weapon type {weapon_type} is not in: {WeaponTypes.joined()}')


class IncompatibleWeaponHeroType(Exception):
    def __init__(self, weapon_type: str, hero_classname: str) -> None:
        super().__init__(f'Weapon type {weapon_type} can\'t be used by hero with type {hero_classname}')


class WeaponTypes:
    types = 'melee', 'range', 'magic'
    @classmethod
    def joined(cls) -> str:
        return ', '.join(cls.types)


class Weapon:
    def __init__(self, title:str, w_type: str) -> None:
        self.title, self.type = title, w_type

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.title} {self.type}'
    
    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, new_type: str) -> None:
        if new_type not in WeaponTypes.types:
            raise InvalidWeaponType(new_type)
        self._type = new_type


class Hero(ABC):
    melee = range = magic = False

    @abstractmethod
    def __init__(self, name: str, weapon: Weapon) -> None:
        self.name, self.weapon = name, weapon

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} with {self.weapon}'
    
    @property
    def weapon(self) -> Weapon:
        return self._weapon
    
    @weapon.setter
    def weapon(self, new_weapon: Weapon) -> None:
        if not isinstance(new_weapon, Weapon):
            raise TypeError(f'Hero expects weapon to be Weapon instance, not {type(new_weapon).__name__}')
        if not getattr(self, new_weapon.type):
            raise IncompatibleWeaponHeroType(new_weapon.type, self.__class__.__name__)
        self._weapon = new_weapon

class Melee(Hero):
    melee = True

class Ranged(Hero):
    range = True

class Sorcerer(Hero):
    magic = True

class Elf(Ranged, Sorcerer):
    def __init__(self, name: str, weapon: Weapon) -> None:
        super().__init__(name, weapon)

class Barbarian(Melee):
    def __init__(self, name: str, weapon: Weapon) -> None:
        super().__init__(name, weapon)


sword, bow, wand, axe = (
    Weapon('King Arguns match', 'melee'),
    Weapon('Onion', 'range'),
    Weapon('shoots once a year', 'magic'),
    Weapon('Axe magic', 'melee')
)

print(Elf('Tyurin', bow))
print(Barbarian('VaviLove', axe))
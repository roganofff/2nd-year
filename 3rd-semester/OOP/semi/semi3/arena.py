from typing import Any, Optional
import random

def check_positive(value: Any, classes=tuple):
    if not isinstance(value, classes):
        classnames = ' '.join([cls.__name__ for cls in classes])
        raise TypeError(f'{type(value).__name__} is not in {classnames}')
    if value < 0:
        raise ValueError(f'value {value} < 0')
    
class HeroNotFoundError(Exception):
    pass

class Weapon:
    def __init__(self, title: str, damage: int|float):
        self.title, self.damage = title, damage

    @property
    def damage(self) -> int|float:
        return self._damage
    
    @damage.setter
    def damage(self, new_damage: int|float) -> None:
        check_positive(new_damage, (int, float))
        self._damage = new_damage


class Hero:
    def __init__(self, name: str, health: int|float = 100,
                weapon: Optional[Weapon] = None, attack: int|float = 10):
        
        self.weapon, self.name, self.health, self.__default_damage = \
            weapon, name, health, attack
        
    @property
    def weapon(self) -> Weapon:
        return self._weapon
    
    @weapon.setter
    def weapon(self, new_weapon: Weapon) -> None:
        if new_weapon is None:
            self._weapon = None
            return
        if not isinstance(new_weapon, Weapon):
            raise TypeError(f'{type(new_weapon).__name__} is not a Weapon inst')
        self._weapon = new_weapon

    @property
    def health(self) -> int|float:
        return self._health
    
    @health.setter
    def health(self, new_health: int|float) -> None:
        check_positive(new_health, (int, float))
        self._health = new_health

    @property
    def damage(self) -> int|float:
        real_dmg = self.weapon.damage if self.weapon else self.__default_damage
        delta = real_dmg / 10
        return real_dmg + random.uniform(-delta, delta)
    
    def pvp(self, other) -> int:
        
        if not isinstance(other, type(self)):
            other_cls = type(other).__name__
            raise TypeError(f'Hero {self.name} cannot fight with {other_cls}')
        
        hero_weapon = self.weapon.title if self.weapon else ""
        other_weapon = other.weapon.title if other.weapon else ""
        print(f'{self.name} with {hero_weapon} ({self.damage} dmg)')
        print(f'{other.name} with {other_weapon} ({other.damage} dmg)')
        hero_hp, other_hp = self.health, other.health
        while hero_hp > 0 and other_hp > 0:
            hero_hp -= other.damage
            other_hp -= self.damage

        print(f'\n PVP {self.name} vs {other.name} finished by')
        if hero_hp <= 0 and other_hp <= 0:
            print('DRAW')
            return 0
        elif hero_hp <= 0:
            print(f'{other.name} victory')
            return 2
        else:
            print(f'{self.name} victory')
            return 1
        
class Arena:
    def __init__(self, heroes: list[Hero]):
        self.heroes = heroes

    def check_hero(self, instance: Any) -> None:
        if not isinstance(instance, Hero):
                raise TypeError(f'{type(instance).__name__} is not a Hero')

    @property
    def heroes(self) -> list[Hero]:
        return self._heroes
    
    @heroes.setter
    def heroes(self, new_heroes: list[Hero]) -> None:
        for hero in new_heroes:
            self.check_hero(hero)
        self._heroes = new_heroes

    def add_hero(self, hero: Hero) -> None:
        self.check_hero(hero)
        self._heroes.append(hero)

    def remove_hero(self, hero: Hero) -> None:
        self.check_hero(hero)
        if hero not in self._heroes:
            raise HeroNotFoundError(f'{hero.name} was not found in Arena Heroes')
        self._heroes.remove(hero)

    def start(self) -> None:
        print('Please greet warmly our noble Arena Heroes!')
        for index, hero in enumerate(self.heroes):
            print(f'{index+1}: {hero.name} {hero.health} with weapon \
                   {str(hero.weapon)} ({hero.damage} dmg)')
            
        points = {hero: 0 for hero in self.heroes}
        for hero_idx in range(len(self.heroes)):
            for other_idx in range(hero_idx+1, len(self.heroes)):
                result = self.heroes[hero_idx].pvp(self.heroes[other_idx])
                if result == 0:
                    points[self.heroes[hero_idx]] += 1
                    points[self.heroes[other_idx]] += 1
                elif result == 1:
                    points[self.heroes[hero_idx]] += 3
                elif result == 2:
                    points[self.heroes[other_idx]] += 3
        print('Arena battle has finished! Glory to brave Heroes!')
        heroes_by_pts = sorted(points.items(), key=lambda item: item[1], reverse=True)
        for index, item in enumerate(heroes_by_pts):
            print(f'{index+1}: {item[0].name} points: {item[1]}')

names = 'Tyurin', 'Vavilov', 'Evstifeev', 'Tyapkova', 'Kolkaryova', 'Kuznetsova'
weapon_names = 'spoon', 'fork', 'chair', 'flowers', 'plastic cup', 'laptop'
weapons = [Weapon(title, random.randint(15, 100)) for title in weapon_names]
weapons += [None]
heroes = [Hero(name, weapon=random.choice(weapons)) for name in names]

Arena(heroes).start()



    
 



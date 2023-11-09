from typing import Any


class Driving:
    def __init__(self, speed: int | float) -> None:
        self.speed = speed

    def drive(self, distance: int | float) -> float:
        time = distance / self.speed
        print(f'Drove you there in {time} time')
        return time
    
class Washing:
    def __init__(self, time_per_item: int | float) -> None:
        self._time_per_item = time_per_item

    def wash(self, items: list[Any]) -> int | float:
        time = 0
        for item in items:
            print(f'Washing time {item}')
            time += self._time_per_item
        print(f'Washed {len(items)} in {time} time')
        return time
    
class Machine:
    def __init__(self, charge_per_time: int | float) -> None:
        self._charge_per_time = charge_per_time
        self.charge_level = 0

    def charge(self, time: int | float) -> int | float:
        new_charge_level = self.charge_level + time * self._charge_per_time
        new_charge_level = new_charge_level if  new_charge_level < 100 else 100
        self.charge_level = new_charge_level
        print(f'Charged to {new_charge_level}')

class WashingMachine(Washing, Machine):
    def __init__(self, charge_per_time: int | float, time_per_item: int | float) -> None:
        super(WashingMachine, self).__init__(time_per_item)
        super(Washing, self).__init__(charge_per_time)

hansa = WashingMachine(50, 0.00001)
hansa.charge(1)
hansa.wash(['pants', 'shirt', 'hat'])
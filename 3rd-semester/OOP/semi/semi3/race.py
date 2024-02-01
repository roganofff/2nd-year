from random import randint
import time
class Counter:
    def __init__(self):
        self.__value = 0
    @property
    def value(self) -> int:
        return self.__value
    
    def increment(self) -> None:
        self.__value += 1
    

    def reset(self) -> None:
        self.__value = 0

    def decrease_value(self) -> None:
        self.__value -= 1
    
my_counter = Counter()







#race

#Car

class Car:
    def __init__(self, model: str, speed: int|float):
        self.model, self.speed = model, speed

    @property
    def speed(self) -> int|float:
        return self._speed
    
    @speed.setter
    def speed(self, new_speed) -> None:
        if not isinstance(new_speed, (int, float)):
            raise TypeError(f'{type(new_speed).__name__} is not int|float')
        if new_speed < 0:
            raise ValueError(f'speed of car {self.model} {new_speed} < 0')
        self._speed = new_speed

class Race:
    def __init__(self, cars: list[Car], laps: int = 5, crash_probability: int = 40):
        self.cars, self.laps, self.crash_probability = cars, laps, crash_probability
        self.__counter = Counter()


    @property
    def cars(self) -> list[Car]:
        return self._cars
    
    @cars.setter
    def cars(self, new_cars: list[Car]) -> None:
        for car in new_cars:
            if not isinstance(car, Car):
                raise TypeError(f'{type(car).__name__} is not a Car instance')
        self._cars = new_cars
    
    def check_positive_int(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f'{type(value).__name__} is not int')
        if value < 0:
            raise ValueError(f'value {value} is less than zero')
    
    @property
    def laps(self) -> int:
        return self._laps

    @laps.setter
    def laps(self, new_laps: int) -> None:
        self.check_positive_int(new_laps)
        self._laps = new_laps
    
    @property
    def crash_probability(self) -> int:
        return self.__crash_probability
    
    @crash_probability.setter
    def crash_probability(self, new_crash_probability: int) -> None:
        self.check_positive_int(new_crash_probability)
        if new_crash_probability > 100:
            raise ValueError(f'Crash probability {new_crash_probability} > 100')
        self.__crash_probability = new_crash_probability
    
    def is_crash_happened(self) -> bool:
        return randint(0, 99) < self.crash_probability
    
    def start(self) -> None:

        if not self.laps:
            print('Race was initialized with zero laps')
            return
        cars = sorted(self.cars, key=lambda car: car.speed, reverse=True)
        print('Please great warmly our race patricipants!')
        for index, car in enumerate(self.cars):
            print(f'{index+1}. {car.model}: {car.speed}')

        while cars and self.__counter.value < self.laps:
            if self.is_crash_happened():
                crashed = cars.pop(randint(0, len(cars)-1))
                print(f'Car {crashed.model} has crashed on lap {self.__counter.value +1}')
                time.sleep(1)

            self.__counter.increment()
        self.__counter.reset()
        if cars:
            for index, car in enumerate(cars):
                print(f'{index+1}: {car.model}')
        else:
             print('All cars have crashed in this deadly race... :/')

carnames = ('Porsche 911', 'Tesla Cybertruck', 'Belaz', 
'Lada 2109 GT Turbo', 'Lada Priora (color = black) (low)', 'TrackTore', 'Zakhar 4x4') 

cars = [Car(name, randint(50, 400)) for name in carnames]

Race(cars).start()
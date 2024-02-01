import random
import time

DELAY = 1

# счётчик Counter
class Counter:
    def __init__(self) -> None:
        self.__value = 0

    @property
    def value(self) -> int:
        return self.__value
    
    def increment(self) -> None:
        self.__value += 1

    def reset(self) -> None:
        self.__value = 0

class Car:
    def __init__(self, model: str, speed: int|float) -> None:
        self.model, self.speed = model, speed

    @property
    def speed(self) -> int|float:
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if not isinstance(new_speed, (int, float)):
            raise TypeError(f'Speed {type(new_speed).__name__} is not int|float.')
        if new_speed < 0:
            raise ValueError(f'Speed of car {self.model} {new_speed} < 0.')
        self._speed = new_speed

    def is_crash(self, prob: int) -> None:
        new_prob = prob * self.speed / 100 if self.speed > 100 else prob
        return random.randint(0, 99) < new_prob

litvinov = Car('litvinov', 20)
print(litvinov.speed)

class Race:
    def __init__(self, cars: list[Car], laps: int = 5, crash_prob: int = 40):
        self.cars, self.laps, self.crash_prob = cars, laps, crash_prob
        self.__counter = Counter()

    @property
    def cars(self) -> list[Car]:
        return self._cars
    
    @cars.setter
    def cars(self, new_cars: list[Car]) -> None:
        for car in new_cars:
            if not isinstance(car, Car):
                raise TypeError(f'{type(car).__name__} is not a  Car instance.')
        self._cars = new_cars

    def check_positive_int(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f'{type(value).__name__} is not int.')
        if value < 0:
            raise ValueError(f'Value {value} is less than zero.')
        
    @property
    def laps(self) -> int:
        return self._laps
    
    @laps.setter
    def laps(self, new_laps) -> None:
        self.check_positive_int(new_laps)
        self._laps = new_laps

    @property
    def crash_prob(self) -> int:
        return self.__crash_prob
    
    @crash_prob.setter
    def crash_prob(self, new_crash_prob) -> None:
        self.check_positive_int(new_crash_prob)
        if new_crash_prob > 100:
            raise ValueError(f'Crash probability {new_crash_prob} > 100.')
        self.__crash_prob = new_crash_prob
    
    def start(self) -> None:
        if not self.laps:
            print('Race was initialized with zero laps.')
            return

        cars = sorted(self.cars, key=lambda car: car.speed, reverse=True)
        print('Please greet warmly our Race participants!')
        for ind, car in enumerate(cars):
            print(f'{ind + 1}. {car.model}: {car.speed}')

        while cars and self.__counter.value < self.laps:
            crashed = []
            for car in cars:
                if car.is_crash(self.crash_prob):
                    crashed.append(car)
            for car in crashed:
                cars.remove(car)
                print(f'Car {car.model} has crashed on lap {self.__counter.value + 1}')
            self.__counter.increment()
            time.sleep(DELAY)

        self.__counter.reset()

        if cars:
            for ind, car in enumerate(cars):
                print(f'{ind + 1}: {car.model}')
        else:
            print('All cars have crashed in this deadly race.')


carnames = (
    'Porshe 911', 'Tesla CyberTruck', 'BeeLus', 'Lada 2107 GT Turbo (color: cherry)',
    'Lada Priora (color: black) (low)', 'TrackTore', 'Zakhar 4x4',
)
cars = [Car(name, random.randint(50, 200)) for name in carnames]
Race(cars, laps=8, crash_prob=10).start()

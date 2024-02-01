from typing import Callable
from utils import Position
from people import Client
from people import Driver
from taxi import Taxi
from car import Car, RegistrationNumber


class Service:
    def __init__(self):
        self._taxi = Taxi()

    def add_driver(self, args: list[str]) -> str:
        name = args[0]
        car_model = input('Type car model: ')
        car_class = input('Car service class: ')
        letters, number, region, country = input('Type license plate in format AAA 111 23 RU: ').split()
        license_plate = RegistrationNumber(number, letters, int(region), country)
        driver = Driver(name, Car(car_model, license_plate, car_class))
        self._taxi.add_driver(driver)
        return f'Driver {driver} successfully added to taxi service.'
    
    def show_drivers(self, *_) -> str:
        return '\n'.join([f'{i + 1}. {driver}' for i, driver in enumerate(self._taxi.drivers)])
    
    def remove_driver(self, args: list[str]) -> str:
        name = args[0]
        self._taxi.remove_driver(name)
        return f'Drivers with name={name} was removed.'

    def add_client(self, args: list[str]) -> str:
        if len(args) == 1:
            self._taxi.add_client(Client(args[0], float(args[1])))
            return f'Client {args[0]} was added successfully.'
        elif len(args) == 4:
            position = Position(float(args[2]), float(args[3]))
            self._taxi.add_client(Client(args[0], float(args[1]), position))
            return f'Client {args[0]} was added successfully.'
        return f'add_client do not take {len(args)} parameters.'
    
    def remove_client(self, args: list[str]) -> str:
        name = args[0]
        self._taxi.remove_client(name)
        return f'Client with name={name} was removed.'
    
    def request_ride(self, args: list[str]) -> str:
        client_name, x, y = args
        for client in self._taxi.clients:
            if client.name == client_name:
                break
        else:
            raise ValueError(f'client with name {client_name} was not found.')
        self._taxi.process_ride(client, Position(float(x), float(y)))
        return 'Ride requested.'
    
    def parse_command(self, command: str):
        commands: dict[str, Callable] = {
            'add_driver': self.add_driver,
            'show_drivers': self.show_drivers,
            'remove_driver': self.remove_driver,
            'register_client': self.add_client,
            'remove_client': self.remove_client,
            'request_ride': self.request_ride,
            # 'cancel_ride': self.cancel_ride,
            # 'exit': self.exit
        }
        splitted = command.split()
        if not splitted:
            return ''
        if len(splitted) > 1:
            command, args = splitted[0], splitted[1:]
        else:
            command, args = splitted[0], None
        for command_key in commands.keys():
            if command == command_key:
                return commands[command_key](args)
        return f'Command {command}not found.'

    def start(self) -> None:
        while True:
            try:
                print(self.parse_command(input()))
            except Exception as error:
                print(error)

if __name__ == '__main__':
    Service.start()
class WorkerNotFound(Exception):
    def __init__(self, power) -> None:
        super().__init__(f'Worker not found for {power} power.')

class Worker:
    def __init__(self, name: str, power: float | int) -> None:
        self.name, self.__power = name, power

    def __call__(self, number: float | int) -> float | int:
        return number ** self.power
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} raises to {self.power} power.'

    @property
    def power(self) -> int:
        return self.__power
    
    @power.setter
    def power(self, new_power: float | int) -> None:
        if not isinstance(new_power, (float, int)):
            raise TypeError(f'{type(new_power).__name__} should be float or int')
        self.__power = new_power

class Boss:
    def __init__(self, name: str, workers: list[Worker]) -> None:
        self.name, self.workers = name, workers

    def __call__(self, data: list[tuple[int]]) -> list[int | float]:
        result = []
        for num, power in data:
            for worker in self.workers:
                if power == worker.power:
                    result.append(worker(num))
                    break
            else:
                raise WorkerNotFound(power)
        return result

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} with {len(self.workers)} workers.'
    
    def add_worker(self, new_worker: Worker) -> None:
        if not isinstance(new_worker, Worker):
            raise f'{new_worker} is not a Worker.'
        self.workers.append(new_worker)

    def remove_worker(self, fired_worker: Worker) -> None:
        if not isinstance(fired_worker, Worker):
            raise f'{fired_worker} is not a Worker.'
        self.workers.remove(fired_worker)

    @property
    def workers(self) -> list[Worker]:
        return self.__workers
    
    @workers.setter
    def workers(self, new_workers: list[Worker]) -> None:
        if not isinstance(new_workers, (list, tuple)):
            raise TypeError(f'List or tuple should be given, got {type(new_workers).__name__} instead.')
        for worker in new_workers:
            if not isinstance(worker, Worker):
                raise TypeError(f'{type(worker).__name__} should be Worker')
        self.__workers = new_workers

boss = Boss('Yegor', [Worker('Zakhar', 6), Worker('Bogdan', 7), Worker('Slavik', 4)])
print(boss([(4, 7), (6, 4)]))

worker = Worker('Dart Weider', 2)
boss.add_worker(worker)
print(*boss.workers)
boss.remove_worker(worker)
print(*boss.workers)

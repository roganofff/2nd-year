from typing import Self


class DownwardCounter:
    def __init__(self, start: int) -> None:
        self._set_start(start)
        self._current = self._start

    def _set_start(self, start: int) -> None:
        msg = f'{self.__class__.__name__} expects start to be '
        if not isinstance(start, int):
            raise TypeError(f'{msg}integer')
        if start < 0:
            raise ValueError(f'{msg}positive')
        self._start = start

    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> int:
        if not self._current:
            self._current = self._start
            raise StopIteration
        self._current -= 1
        return self._current + 1

counter = DownwardCounter(2)
for value in counter:
    print(value)
for value in counter:
    print(value)
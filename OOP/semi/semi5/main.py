from time import ctime
import os
from typing import Any

class TermialOpener:
    __counter = 0

    def __init__(self) -> None:
        self.__calls = []
        self.__class__.__counter += 1

    def __call__(self):
        if os.system('gnome-terminal'):
            print('Gnome terminal failed to start.')
        else:
            self.__calls.append(ctime())

    def __del__(self):
        self.__class__.__counter -= 1
        del self

    @property
    def calls(self) -> list[str]:
        return self.__calls
    
    @property
    def calls_counter(self) -> int:
        return len(self.__calls)
    
    @classmethod
    def counter(cls) -> int:
        return cls.__counter

opener = TermialOpener()

for _ in range(208):
    opener()

print(opener.calls[0], opener.calls[-1], opener.calls_counter)                 
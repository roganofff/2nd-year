from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def sleep(self) -> None:
        pass

    @abstractmethod
    def study(self) -> None:
        pass


class Sleeping(State):
    def eat(self) -> None:
        print('Cannot eat now, I\'m sleeping.')

    def sleep(self) -> None:
        print('Already sleeping.')

    def study(self) -> None:
        print('Studying in my dreams.')


class Eating(State):
    def eat(self) -> None:
        print('Already eating.')

    def sleep(self) -> None:
        print('Cannot sleep right now, wait a bit.')

    def study(self) -> None:
        print('Uuuuuuuuuuuuuuuuuuuuuuuuh')

class Studying(State):
    def eat(self) -> None:
        print('DO NOT BOTHER ME WITH YOUR FOOD, I AM STUDYING')

    def sleep(self) -> None:
        print('No time to sleep')

    def study(self) -> None:
        print('Studying twice as hard.')


class Student:
    def __init__(self, name: str, state: State = Studying()) -> None:
        self.name, self.state = name, state

    @property
    def state(self) -> None:
        return self.__getstate__

    @state.setter
    def state(self, new_state: State) -> None:
        if not isinstance(new_state, State):
            raise TypeError('Student state should be State instance.')
        self._state = new_state

    def eat(self) -> None:
        self.state.eat()
        
    def sleep(self) -> None:
        self.state.sleep()
        
    def study(self) -> None:
        self.state.study()


krdyan = Student('Программист на юнити (игры пишет)', Sleeping)
krdyan.state = Sleeping()
krdyan.sleep()
# припипрпирприприпрпрпип прнивет привет как твои дела 😊😊😊😊😊😊😊😊😊😊😊😊 егоррррррррорр ррррррррр   


#  какая прикольная вееешь аааа 
# и такая мидлая 
# и зщвук такой проиятный 
# я почти что привыкла к клавиатуре 
# мне просто нравится чтото печатать 
# я не щнаб что еще написатать 
# я хотнелап написать напечатать но написаоа еаписатиь  сколько ошиьрк цудлвасавччччссс
# ужас ошибок  
# каак твои делоа егор ???
# а что ты ищучае6шь ?*? изучаешть вхвхвхвхвхвхвхвхвхвх 
# а почему у тебя тут не фиолетовакя тема???**????????? кггоооооооолоррпррррррррр егор егогр егор егор егор егор егнор егор егор егор егоре 
# почвему не фиолдетовая ? е
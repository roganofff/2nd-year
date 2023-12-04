from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def study(self):
        pass


class Sleeping(State):
    def eat(self):
        print("Cannot eat now, I'm sleeping")

    def sleep(self):
        print('Already sleeping')

    def study(self):
        print('Study in mmy dreams')


class Eating(State):
    def eat(self):
        print('Already eating')

    def sleep(self):
        print('Cannot slep rn, wait a bit')

    def study(self):
        print('Watching mCoding')


class Suding(State):
    def eat(self):
        print('Do not Bthore me with food, i am sudying')

    def sleep(self):
        print('No time to sleep, i am studing')

    def study(self):
        print('Suding twice as hard')

class Student:
    def init(self, name, state: State) -> None:
        self.name, self.state = name, state

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, new_state):
        if not isinstance(new_state, State):
            raise TypeError()
        self._state = new_state

    def eat(self):
        self.state.eat()

    def sleep(self):
        self.state.sleep()

    def study(self):
        self.state.study()


krdyan = Student('Программист на Unity', Eating())
a = Eating()
krdyan.state = a
krdyan.sleep()
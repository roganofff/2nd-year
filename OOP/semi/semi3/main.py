class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age
    
    def walk(self, miles: float) -> None:
        print(f'{self.__class__.__name__} {self.name} walked for {miles} miles')

class Student(Person):
    study_rate = 50
    sleep_rate = 30
    eat_rate = 0.15
    danger_level = 500
    def __init__(self,name: str, age: int, group: str) -> None:
        super().__init__(name,age)
        self.group = group
        self.tiredness = 0

    def message(self, msg: str) -> None:
        print(f'{type(self).__name__} {self.name}: {msg}')
        

    def check_tiredness(self):
        if self.tiredness > self.danger_level:
            self.message(f'tiredness {self.tiredness} > {self.danger_level}')

    def study(self, hours: float) -> None:
        self.tiredness += hours * self.study_rate
        self.message (f'was studying for {hours} hours')
        self.message (f'tiredness increassed to {self.tiredness}')
        self.check_tiredness()

    def restore(self, restorations: float) -> None:
        new_tiredness = self.tiredness - restorations
        self.tiredness = new_tiredness if new_tiredness > 0 else 0
        self.message(f'tiredness decreassed to {self.tiredness}')

    def sleep(self, hours: float = 7.5) -> None:
        self.message(f'was sleeping for {hours} hours')
        self.restore(hours * self.sleep_rate)
        
    def eat(self,kcal: float) -> None:
        self.message(f'has eaten for {kcal} kcal')
        self.restore(kcal * self.eat_rate)

startsev = Student('Zakhar', 16, '1.9.7.2')
startsev.study(11)
startsev.eat(2170)
startsev.sleep(7.5)
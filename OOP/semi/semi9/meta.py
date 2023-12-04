import json


class JSONableMeta(type):
    def __init__(cls, *_):
        def to_json(self) -> str:
            return json.dumps(self.__dict__)
        
        def from_json(cls, json_attr: str):
            return cls(**json.loads(json_attr))
        
        cls.to_json = to_json
        cls.from_json = classmethod(from_json)
        
class Person(metaclass=JSONableMeta):
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

print(Person.from_json(Person('Slavic', 18).to_json()).name)

A = type('A', (object, ), {'attr': 10, 'method': lambda : print('slavic')})
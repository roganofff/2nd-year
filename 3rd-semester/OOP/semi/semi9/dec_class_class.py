import json
from typing import Self

class JSONable:
    def __new__(_, class_: type) -> Self:
        def to_json(self) -> str:
            return json.dumps(self.__dict__)
        
        def from_json(cls, json_attr: str):
            return cls(**json.loads(json_attr))
        
        setattr(class_, 'to_json', to_json)
        setattr(class_, 'from_json', classmethod(from_json))
        return class_
    
@JSONable
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

print(Person.from_json(Person('Slavic', 18).to_json()).name)

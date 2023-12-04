def comparable(attr):
    def decorator(cls):
        dunder_methods = '__lt__', '__le__', '__gt__', '__ge__', '__eq__', '__ne__'
        def create_dunder(method):
            def dunder_method(self, other):
                return getattr(getattr(self, attr), method)(getattr(other, attr))
            return dunder_method
        for method in dunder_methods:
            setattr(cls, method, create_dunder(method))
        return cls
    return decorator

def check_name(name: str) -> None:
    if not isinstance(name, str):
        raise TypeError(f'Wrong type of name, expecting str, got {type(name).__name__} instead')
    for c in name:
        if c.isdigit():
            raise ValueError(f'Name cannot contain digits')
        
def check_positive(number: int) -> None:
    if not isinstance(number, int):
        raise TypeError(f'Wrong type of number, expecting int, got {type(number).__name__} instead')
    if number < 0:
        raise ValueError(f'{number} should be positive')

checkers = [check_name, check_positive]

def add_property(attr, checkers):
    def decorator(cls):
        def setter(self, value):
            for checker in checkers:
                checker(value)
            setattr(self, f'_{attr}' , value)
        def getter(self):
            return getattr(self, f'_{attr}')
        setattr(cls, attr, property(getter, setter))
        return cls
    return decorator
        
def stringify(cls):
    def string_method(self):
        res = f'{cls.__name__}'
        for attr, value in self.__dict__.items():
            if not callable(value):
                res += f' {attr}=<{value}>'
        return res
    setattr(cls, '__str__', string_method)
    return cls

@stringify
@add_property('age', [check_positive])
@add_property('name', [check_name])
@comparable('age')
class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

vasya = Student('Petro Aleksiyovich', 40)
vano = Student('Ivan Stepanovich', 10)
print(vasya, vano, sep='\n')
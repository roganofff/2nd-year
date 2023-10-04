from typing import Callable
from functools import wraps

# def f(a, b, c, d, e, f):
#     print(a, b, c, d, e, f)


# def f(*args, **kwargs):
#     print(*args, kwargs)

# f(1, 2, 3, 4, f=6, e=5)

def info(func: Callable) -> Callable:
    @wraps(func)
    def new(*args, **kwargs):
        print(f'Running function {func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result for {func.__name__} is {result}')
        return result
    return new

def create_text(*words, sep: str = ', ', end: str = '!') -> str:
    """Create text from words using separator and text ending."""
    return sep.join(words) + end


print(create_text.__doc__)
create_text = info(create_text)
print('After decorator:\n', create_text.__doc__, sep='')

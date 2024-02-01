# Декоратор - это функция, которая возвращает новую функции, добавляя к её выполнению дополнительный функционал.
# Простейший декоратор: отрожающий основные параметры функции(название, принятые аргументы и прочее)

def show(func):
    def new_func(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Key words arguments are: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_func


@show
def my_sum(a: int|float, b: int|float) -> int|float:
    return a + b


print(my_sum(5, 6.7))
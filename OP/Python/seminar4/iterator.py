from typing import Tuple
# nums = [1, 2, 3, 5]
# iterator = iter(nums)

# for value in iter(nums)
# for value in iterator:
#     print(value)

# simple lambda
f = lambda x: x*x

def agree():
    return True
# print(agree())

# u may put no args
agree_ = lambda: True
# print(agree_())

counter = 11
def show_counter():
    return f'Current counter is {counter}'
# lambda that uses global variables
show_counter_ = lambda: f'Current counter is {counter}'

# lambda with multiple return values
def get_counter():
    return (f'Current counter: {counter}', \
        f'Half is: {round(counter / 2)}')
# print(*get_counter())


get_counter_ = lambda: (f'Current counter: {counter}', \
        f'Half is: {round(counter / 2)}')
# print(*get_counter_())

# lambda with multiple input arguments
def sum_points(a: Tuple[int], b: Tuple[int]):
    return a[0] + b[0], a[1] + b[1]
# print(sum_points((1, 1), (2, 3)))

sum_points_ = lambda a, b: (a[0] + b[0], a[1] + b[1])
# print(sum_points_((1, 1), (2, 3)))

# lambda with positional and keyword agruments
def return_args(*args, **kwargs):
    return args, kwargs
# print(return_args(1, 2, 3, a=5, b=90))


return_args_ = lambda *args, **kwargs: (args, kwargs)
# print(return_args_(1, 2, 3, a=5, b=90))

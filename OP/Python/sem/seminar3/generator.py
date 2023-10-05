from typing import Generator
from sys import getsizeof

# nums = [i for i in range(10**6)]
# # print(type(nums))
# memory = getsizeof(nums) + sum(getsizeof(item) for item in nums)

# print(memory // (2**13))

# range_mil = range(10**6)
# # print(type(range_mil))
# print(getsizeof(range_mil))

# def range_(end: int, start: int = 0, step: int = 1) -> Generator:
#     while step > 0 and start < end or step < 0 and start > end:
#         yield start
#         start += step
# 
# range_five = range_(5)
# 
# i = 0
# for value in range_five:
#     if i > 2:
#         range_five.throw(Exception('слишком тупой'))
#     print(value)
#     i += 1# 

######################

# def gen():
#     for _ in range(3):
#         x = yield
#         yield x + 1



# generator = gen()
# for value in generator:
#     print(generator.send(1))

###############################

# fibonacci 
# def fibonacci(n: int) -> Generator:
#     fst, snd = 0, 1
#     yield fst

#     while n > 1:
#         yield snd
#         fst, snd = snd, fst + snd
#         n -= 1
        
# for index, value in enumerate(fibonacci(5)):
#     print(f'{index+1} элемент Фибоначчи = {value}')

##################

# def half_life(years: int|float) -> Generator:
#     amount, time = 100, 0
#     while True:
#         yield amount, time
#         amount /= 2
#         time += years


# i = 0
# for amount, time in half_life(1000):
#     print(f'Через {time} лет останется {amount}% вещества.')
#     if i > 10:
#         break
#     i += 1

###################

# from datetime import date

# def is_leap(year: int) -> bool:
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)  

# def leap_years() -> Generator:
#     year = date.today().year
#     while not is_leap(year):
#         year += 1
    
#     while True:
#         if year % 100 != 0 or year % 400 == 0:
#             yield year
#         year += 4 


# for index, year in enumerate(leap_years()):
#     if index > 20:
#         break
#     print(year)

# генератор принимающий n и power:
# генериррует степени n положительных чисел, от 0 и тд
# gen(4, 3) -> 0, 1, 8, 27
# gen(5, 2) -> 0, 1, 4, 9, 16

def gen(n: int, power: int) -> Generator:
    i = 0
    while i < n:
        yield i ** power
        i += 1
    
power = 2
for num, product in enumerate(gen(5, power)):
    print(f'{num} в степени {power} = {product}')
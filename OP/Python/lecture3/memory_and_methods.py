from sys import getsizeof

numbers = []
mem = 0

# for _ in range(100):
#    new_mem = getsizeof(numbers)
#    if new_mem > mem:
#        mem = new_mem
#        print(mem, len(numbers))    
#    numbers.append(1)

full_memory  = getsizeof(numbers) + sum([getsizeof(item) for item in numbers])
# список в питоне - динамический несвязный список.

# print("dsds dsds".title())  --  Dsds Dsds
# print("dsds dsds".capitalize())  --  Dsds dsds
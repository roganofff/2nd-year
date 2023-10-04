# 1
# print(file.readlines())

# 2
# for _ in range(2):
#     print(file.readline())

# 3
# for line in file.readlines():
#     print(line)

# 4
# for line in file:
#     print(line)

# modes: r - read, w - write, a - add

# file = open('text.txt', 'a')

# lines = [
#     'Android is versatile',
#     'Astra Linux is a friend of College Sirius', 
# ]

# lines = [f'{line}\n' for line in lines]
# for line in lines:
#     file.write(line)

# file.close()

source = 'text.txt'
output = 'new_text.txt'

with open(source, 'r') as source_file, open(output, 'w') as out_file:
    out_file.write(source_file.read())
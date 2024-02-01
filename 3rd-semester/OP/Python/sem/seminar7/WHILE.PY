from string import ascii_letters

result = []
print(len(ascii_letters))
n = 0
step = 1
while True:
    result.append(ascii_letters * n)
    if n == 99:
        step = -1
    elif n == 0:
        step = 1
    n += step 
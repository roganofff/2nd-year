funcs_pow = []

QUANTITY = 4

for pow_ in range(QUANTITY):
    funcs_pow.append(lambda num: num ** pow_)

number = 2
print([func(number) for func in funcs_pow])

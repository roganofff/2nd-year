def M(n):
    if n == 0:
        return 0
    if n < 0:
        return -1
    return n - F(M(n - 1))

def F(n):
    if n == 0:
        return 1
    if n < 0:
        return -1
    return n - M(F(n - 1))
    

print(M(9))
print(F(9))

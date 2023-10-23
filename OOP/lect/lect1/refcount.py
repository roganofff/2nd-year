from sys import getrefcount # reference counter


a = 5
b = a
c = b
print(getrefcount(a))

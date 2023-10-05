# sorted or sort uses lambda

words = ['abc', 'km', 'dmpo']

def len_sort(text: str) -> int:
    return len(text)

print(sorted(words, key=lambda text: len(text), reverse=True))

# map

def square(x: int|float) -> int|float:
    return x*x

nums = [1, 2, 3]
# for value in map(square, nums):
#     print(value)

nums = list(map(square, nums))
# nums = [square(x) for x in nums]   same shit
nums.append(16)
print(nums)

##################

# filter
vowels = 'aiouey'
def has_vowels(text: str) -> bool:
    return any([char in text for char in vowels])

words = ['slkd', 'aoqw', 'jija', 'xqc']
words = list(filter(has_vowels, words))
words = list(filter(lambda text: any([char in text for char in vowels]), words))
print(words)
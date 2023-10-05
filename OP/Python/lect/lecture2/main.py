#title, text = input("Введите название: "), input("Введите текст: ")
#print('{0:*^100}'.format(title))
#print('\t', text.capitalize())
#
#numbers = [i for i in range(1, 10, 2)]

#length = len(numbers)
#index = length
#while index:
#    print(numbers[length - index])
#    index -= 1

"""Main module."""


def make_dict(keys: list, data_values: list):
    """A function that makes a dict from two lists

    Args:
        keys: list - a list of keys
        data_values: list - a list of values
    Returns: 
        dict - created dictionary
    """
    return {key: value for key, value in zip(keys, data_values)}

print(make_dict([1, 2, 3], [1, 5, 7, 4]))
help(make_dict)
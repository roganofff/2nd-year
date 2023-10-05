from string import ascii_lowercase, punctuation
from typing import List

def count_vowels(text: str):
    vowels = 'aeiouy'
    text = text.lower()
    return sum([text.count(vowel) for vowel in vowels])


def contains_all(text: str) -> bool:
    text = text.lower()
    return all(char in text for char in ascii_lowercase)


def get_missing_letters(text: str) -> List[str]:
    text = text.lower()
    return [char for char in ascii_lowercase if char not in text]


def clean(text: str) -> str:
    text = text.lower().replace('\n', ' ')
    for symbol in f'{punctuation}-':
        text = text.replace(symbol, ' ')
    return text


def calculate_statistic(text: str) -> None:
    for lit in punctuation:
        text = text.replace(lit, '')

    stats = dict()
    for word in text.lower().split():
        if word in stats.keys():
            stats[word] += 1
        else:
            stats[word] = 1

    print("Топ 10 слов по списку")
    for key, value in sorted(stats.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{key}:\n\t {value}")


with open("text.txt", "r") as file:
    calculate_statistic(file.read())
    get_missing_letters(file.read())
    contains_all(file.read())
    count_vowels(file.read())
# Лямбда функция - анонимная функция, описанная одним выражением. Её можно использовать вместо обычной маленькой функции.
from typing import List, Callable

a = lambda x : x[0] ** x[1]

print(a((5, 2)))

def edit_story(words: List[str], func: Callable):
    return [func[word] for word in words]

print(edit_story(['python', 'is', 'great'], lambda word: f'{word.capitalize()}!'))
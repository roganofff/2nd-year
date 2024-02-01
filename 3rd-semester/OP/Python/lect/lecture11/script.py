# кот-пример киспользования модулей
# мы принимем имена котов
# скачиваем их ЧЕРЕЗ PYTHON
# записываес в json
# предлагаем выбрать котов для объединения в Общество с Ограниченной Ответственностью
# ООО Кот на Python
# мёрджить изображения котов в одно изображение

import os
import requests # для web-запросов
from PIL import Image # для изображений
from progress.bar import Bar # для отображения прогресса скачивания

cat_names = []
CATAAS_URL = 'https://cataas.com/cat'
OK = 200
EXIT_SEQS = ('q', 'quit', 'exit', 'й')


def write_cat(cat: str, response: requests.Response) -> str:
    filename = os.path.join(directory, f'{cat}.png') 
    with open(filename, 'wb') as cat_file:
        cat_file.write(response.content)

    return filename


def show_cat(filename: str) -> None:
    image = Image.open(filename)
    image.show()


def merge_cats(files: list[str]) -> None:
    images = [Image.open(file) for file in files]
    width = sum([image.size[0]] for image in images)
    height = max([image.size[1]] for image in images)
    new_image = Image.new('RGBA', (width, height))
    cur_width = 0
    for image in images:
        new_image.paste(image, (cur_width,0))
        cur_width += image.size[0]
    new_image.show()


while True:
    name = input('Введите имя очередного кота: ')
    if name.lower() in EXIT_SEQS:
        break
    cat_names.append(name)

if not cat_names:
    print('Вы не ввели имя ни одного кота. =(^,,^)=')
    exit(0)

directory = 'cats'
if not os.path.isdir(directory):
    os.mkdir(directory)
    full_name = os.path.join(os.getcwd(), directory)
    print(f'Директория {full_name} не существует, создаём.')

cats_files = dict()

bar = Bar('Скачиваем котов', max=len(cat_names))

for cat in cat_names:
    response = requests.get(CATAAS_URL)
    if response.status_code == OK:
        filename = write_cat(cat, response)
        cats_files[cat] = filename
        print(f'\nАватарка кота {cat} записана в файл {filename}. (=^･ω･^=)')
    else:
        print(f'\nДля кота {cat} не скачалась аватарка. =^._.^=')
    bar.next()
bar.finish()

cats_menu = ''
for index, cat in enumerate(cat_names):
    cats_menu += f'\n{index+1}. {cat}'

start = 'Выберите кота, которого хотите посмотреть:'
num_cats = len(cat_names)
while True:
    num = input(f'{start}{cats_menu}\n')
    if num.lower() in EXIT_SEQS:
        break

    try:
        index = int(num)
    except ValueError:
        print(f'Вы должны вводить число от 1 до {num_cats}')
    else:
        if index <= 0 or index > num_cats:
            print(f'Вы должны вводить число от 1 до {num_cats}')
        show_cat(cats_files[cat_names[index - 1]])

start = 'Выберите котов-учредителей ООО Кот на Python (через пробел):'
while True:
    indexes = input(f'{start}{cats_menu}\n')
    if indexes.lower() in EXIT_SEQS:
        break

    try:
        indexes = list(map(int, indexes.split()))
    except ValueError:
        print(f'Вы должны вводить число от 1 до {num_cats}')
    else:
        merge_cats([cats_files[cat_names[index - 1]] for index in indexes])
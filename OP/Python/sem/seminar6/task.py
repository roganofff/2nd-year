import os
import json

directory_struct = {'root': {}}
dir_name = input('Структуры какой папки вы хотите сохранить?: ')

keys = ['root']
for path, folders, files in os.walk(dir_name):
    level = path.count('/')
    for index, key in enumerate(keys):
        if index == 0:
            current = directory_struct[key]
        else:
            current = current[key]
    current_dir = path[path.rfind('/')+1:]
    current_dirs = {folder: {} for folder in folders}
    current_files = {file: None for file in files}
    current[current_dir] = dict(**current_dirs, **current_files) 
    keys += current_dir

with open(f'{dir_name}_structure.json', 'w') as json_file:
    json.dump(directory_struct, fp=json_file)
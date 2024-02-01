import os

PATH = '/home/yegor/Documents/2nd-year/OP/Python/sem/'
SEP = '--'

for path, folders, files in os.walk(PATH):
    level = path.count('/') - PATH.count('/')
    print(f"{SEP * level}{path.split('/')[-1]} (D)")
    for file in files:
        print(f"{SEP * (level + 1)}{file} (F)")

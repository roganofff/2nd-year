import os
import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--directory', '-d')
parser.add_argument('--format', '-f', default='txt')

args = parser.parse_args(sys.argv[1:])

try:
    directory = args.directory
except AttributeError:
    print('Directory was not provided.')
    os._exit(1)

if not os.path.isdir(directory):
    print(f'{directory} is not a directory.')

if not os.path.isdir('dataset'):
    os.mkdir('dataset')

cnt = 1
for file in sorted(os.listdir(directory)):
    full_name = os.path.join(os.getcwd(), directory, file)
    if os.path.isfile(full_name) and file.endswith(args.format):
        new_name = f'dataset/{cnt}.{args.format}'
        if not os.system(f'cp {full_name} {new_name}'):
            print(f'File was successfully copied as {new_name}.')
            cnt += 1

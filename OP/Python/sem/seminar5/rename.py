import os
import sys

import argparse
import dotenv

user = os.environ.get('USER', default='yehor')
home = os.environ.get('HOME', default=f'home/{user}')
prefix = os.environ.get('prefix', default='')

print(f'Global environment variable HOME: {home}')
if not prefix:
    print('Prefix was nor provided.')
    os._exit(0)

print(f'Prefix was loaded: {prefix}')

# разбор аргументов командой строки
parser = argparse.ArgumentParser()
dir_help = 'a directory for renaming files'
parser.add_argument('--directory', '-d', default='folder', help=dir_help)
args = parser.parse_args(sys.argv[1:])

if not os.path.isdir(args.directory):
    print(f'{args.directory} is not a directory')
    os._exit(0)

for filename in os.listdir(args.directory):
    full_name = os.path.join(os.getcwd(), args.directory, filename)
    if os.path.isfile(full_name):
        new_name = f'{args.directory}/{prefix}{filename}'
        os.rename(full_name, new_name)
        print(f'File {filename} successfully renamed to {new_name}')
    else:
        print(f'{filename} is not a file!')
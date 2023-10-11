import os
import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t')
parser.add_argument('--source', '-s')

args = parser.parse_args(sys.argv[1:])

target = args.target
source = args.source

if not (os.path.isdir(source) and os.path.isdir(target)):
    print('Given agrument is not a directory.')
    os._exit(1)


def get_file_list(folder: str) -> list:
    return [file for file in os.listdir(folder) if os.path.join(os.getcwd(), folder, file)]


for file in set(get_file_list(target)) & set(get_file_list(source)):
    os.remove(os.path.join(args.target, file))
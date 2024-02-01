import sys

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--number', '-n', help='a number')
parser.add_argument('--greeting', '-g', default='Hello!', help='a greeting')

args = parser.parse_args(sys.argv[1:])
print(args.number, args.greeting)
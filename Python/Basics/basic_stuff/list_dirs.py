# List giles in project directory.
from math import factorial
from os import listdir
from os.path import isfile
from pathlib import Path

home_dir = '.'
path = Path(home_dir)

for f in listdir(path):
    if isfile(f):
        print(f'File: {f}')










def fac(x):
    if x == 1:
        return x
    return x * fac(x-1)
print(fac(52))
print(factorial(52))

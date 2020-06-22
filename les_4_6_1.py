from sys import argv
from itertools import count

script_name, start, end = argv

try:
    start, end = int(start), int(end)
    for i in count(int(start)):
        if i > int(end):
            break
        elif i % 2 == 0:
            print(i)
except ValueError:
    print("Аргументы должны быть целыми числами")

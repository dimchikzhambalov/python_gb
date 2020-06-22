from sys import argv
from itertools import cycle

script_name, end = argv

my_list = ["Я", "люблю", "Python"]
i = 0

try:
    end = int(end)
    for el in cycle(my_list):
        if i >= int(end):
            break
        print(el)
        i += 1
except ValueError:
    print("Аргумент должен быть целым числом")

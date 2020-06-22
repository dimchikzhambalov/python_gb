from math import factorial
from sys import argv

script_name, n = argv


def fact(a):
    try:
        a = int(a)
        for i in range(1, a + 1):
            yield factorial(i)
    except ValueError:
        print("Аргумент должен быть целым числом")


print([el for el in fact(n)])

from functools import reduce


def multi(a, b):
    return a * b


my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(my_list)
print(reduce(multi, my_list))

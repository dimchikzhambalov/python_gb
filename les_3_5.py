def my_func(*args):
    global s, b
    for i in args:
        if i != "!":
            s += int(i)
            b = True
        elif i == "!":
            b = False
    return s, b


s = 0
b = True

while b:
    digits = tuple(input("Введите через пробел несколько чисел, чтобы завершить введите '!': ").split())
    my_func(*digits)
    print(s)

def my_func(var1, var2, var3):
    min_val = min(var1, var2, var3)
    res = var1 + var2 + var3 - min_val
    return print(f"Сумму двух наибольших чисел: {res}")


dig1 = int(input("Введите первое число: "))
dig2 = int(input("Введите первое число: "))
dig3 = int(input("Введите первое число: "))

my_func(dig1, dig2, dig3)

def my_func(x, y):
    return x ** y


def second_func(x, y):
    z = x
    for i in range(1, abs(y)):
        z = z * x
    return 1 / z


a = float(input("Введите действительное положительное число: "))
b = int(input("Введите целое отрицательное число: "))

while b > 0:
    b = int(input("Введите целое отрицательное число: "))

print(my_func(a, b))
print(second_func(a, b))

def div_dig(dig1, dig2):
    res = dig1 / dig2
    return res

while True:
    num1 = int(input("Введите делимое: "))
    num2 = int(input("Введите делитель: "))

    try:
        print(f"Результат деления {num1} на {num2}: ", div_dig(num1, num2))
    except ZeroDivisionError:
        print("Ай-я-яй! На ноль делить нельзя!")

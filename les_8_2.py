class ZeroDivEx(Exception):
    def __init__(self, ex_text):
        self.ex_text = ex_text


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    if b == 0:
        raise ZeroDivEx("A-та-та! На ноль делить нельзя")
except ZeroDivEx as err:
    print(err)
else:
    print(f"Результат деления: {a} / {b} = ", a / b)

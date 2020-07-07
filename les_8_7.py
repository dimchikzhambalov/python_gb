# Из задания не понятно требуется ли использовать функцию complex(), в файле les_8_7.1.py с ней.
# Если делать без функции, то как проверить, что число комплексное?


class ComplexDigit:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __mul__(self, other):
        return self.x * other.x


c1 = ComplexDigit(1 + 3j)
c2 = ComplexDigit(2 + 7j)

print(c1 + c2)
print(c1 * c2)

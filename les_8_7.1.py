class ComplexDigit:
    def __init__(self, x):
        self.x = complex(x)

    def __add__(self, other):
        return self.x + other.x

    def __mul__(self, other):
        return self.x * other.x


c1 = ComplexDigit(2 + 7j)
c2 = ComplexDigit(6)

print(c1 + c2)
print(c1 * c2)

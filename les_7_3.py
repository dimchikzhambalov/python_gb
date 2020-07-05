class Ceil:
    def __init__(self, quan):
        try:
            self.quan = int(quan)
        except ValueError:
            print("Ожидается целочисленное значение")

    def __add__(self, other):
        return self.quan + other.quan

    def __sub__(self, other):
        if self.quan > other.quan:
            return self.quan - other.quan
        elif other.quan > self.quan:
            return other.quan - self.quan
        else:
            print("Значения не должны быть одинаковыми")

    def __mul__(self, other):
        return self.quan * other.quan

    def __truediv__(self, other):
        return round(self.quan / other.quan)

    def make_order(self, rows):
        return '\n'.join(["*" * rows for i in range(self.quan // rows)]) + '\n' + "*" * (self.quan % rows)


c1 = Ceil(15)
c2 = Ceil(23)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c2.make_order(5))

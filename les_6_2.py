class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
        self.mass = 25
        self.height = 5

    def calc(self):
        weight = self._length * self._width * self.mass * self.height
        print(f"Для покрытия дороги длиной {self._length} и шириной {self._width} метров, ")
        print(f"потребуется {weight / 1000} тонн асфальта")


a = Road("df", 20)
a.calc()

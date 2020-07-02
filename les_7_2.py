from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calc(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calc(self):
        return round(self.h * 2 + 0.3, 2)


coat = Coat(48)
costume = Costume(174)

print(coat.calc)
print(costume.calc)


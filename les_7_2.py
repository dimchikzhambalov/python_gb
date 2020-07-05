from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc


class Coat(Clothes):
    @property
    def calc(self):
        print(f"Для пальто {self.size} размера потребуется {round(self.size / 6.5) + 0.5} ткани")
        return round(self.size / 6.5) + 0.5


class Costume(Clothes):
    @property
    def calc(self):
        print(f"Для костюм для роста {self.size} потребуется {round(self.size * 2) + 0.3} ткани")
        return round(self.size * 2) + 0.3


coat = Coat(48)
costume = Costume(174)

print(coat + costume)

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}. Рисуем ручкой.")


class Pensil(Stationery):
    def draw(self):
        print(f"{self.title}. Рисуем карандашом.")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}. Рисуем маркером.")


a = Pen("Big")
b = Pensil("HB")
c = Handle("Blue")

a.draw()
b.draw()
c.draw()

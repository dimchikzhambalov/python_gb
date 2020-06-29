class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Поехали!")

    def stop(self):
        print("Остановились.")

    def turn(self, direction):
        print(f"Поворот {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили допустимую скорость. Сбавьте обороты.")
        else:
            print(f"Текущая скорость автомобиля: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили допустимую скорость. Сбавьте обороты.")
        else:
            print(f"Текущая скорость автомобиля: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, country):
        super().__init__(speed, color, name, is_police)
        self.country = country


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


townCar = TownCar(60, "red", "Toyota Corolla", is_police=False)
workCar = WorkCar(40, "blue", "Трактор 'Белорусь'", is_police=False)
sportCar = SportCar(120, "yellow", "Ferrari F700", is_police=False, country="Italy")
policeCar = PoliceCar(80, "red", "Ford Focus")

print(f"Городской автомобиль: {townCar.name}, цвет: {townCar.color}, полицейский: {townCar.is_police}")
print(f"Спортивный автомобиль {sportCar.name} родом из {sportCar.country}")
workCar.show_speed()
print(policeCar.speed)
policeCar.turn("налево")
print(policeCar.is_police)

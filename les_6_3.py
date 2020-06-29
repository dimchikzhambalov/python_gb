class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.get("salary") + self._income.get("bonus"))


d = Position("Иван", "Денисов", "Директор", 10000, 2000)
s = Position("Василий", "Сидоров", "Бухгалтер", 7000, 3000)
print(d.name)
print(s.surname)
print(d.position)
print(s._income)
d.get_full_name()
s.get_total_income()

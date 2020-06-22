from sys import argv

script_name, hours, sal_per_h, bonus = argv


def calc(a, b, c):
    return (a * b) + c


try:
    hours, sal_per_h, bonus = float(hours), float(sal_per_h), float(bonus)
    print(f"Заработная плата составит: {calc(hours, sal_per_h, bonus)} руб.")
except ValueError:
    print("Переданы некорректные значения параметров для расчета")

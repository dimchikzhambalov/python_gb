name = input("Введите ваше имя: ")
age = int(input("Сколько вам полных лет: "))
wish = input("Ваша самая заветная мечта: ")
done = int(input("Сколько вам будет полных лет, когда она исполниться: "))

dist = done - age

print(name, f" осталось всего {dist} года/лет до исполнения вашей мечты: {wish}.")
print("Думаю следует сосредоточиться на ее достижении! Все обязательно получиться!")

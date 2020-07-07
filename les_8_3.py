class TheDigList(Exception):
    def __init__(self, text):
        self.text = text

my_list = []

while True:
    el = input("Введите значение для добавления в список: ")
    try:
        if el == "stop":
            print(my_list)
            break
        elif not el.isdigit():
            raise TheDigList("В списке должны содержаться только числа!")
        elif el.isdigit():
            my_list.append(el)
    except TheDigList as err:
        print(err)
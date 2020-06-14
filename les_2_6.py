print("Список товаров.")
choice = int(input("Если хотите посмотреть список уже имеющихся товаров введите '1'"
      "\nХотите добавить товар нажмите 'Ввод' или любой символ\nВаш выбор: "))

products = []

if choice == 1:
    print("Текущий список товаров")
elif choice != 1:
    new = 1
    n = 1
    while new != "1":
        name = input("Название товара: ")
        price = int(input("Цена товара: "))
        quantity = int(input("Кол-во товара: "))
        unit = input("Ед.измерения (например, шт.): ")
        prod_dict = {"name": name, "price": price, "quantity": quantity, "unit": unit}
        prod_tuple = (n, prod_dict)
        print(prod_dict)
        n += 1
        new = input("Чтобы чтобы выйти наберите '1', чтобы добавить еще товар введите любой символ: ")
        products.append(prod_tuple)
else:
    print("Спасибо!")
products = [
    (1, {'name': 'Автомобиль', 'price': 500000, 'quantity': 1, 'unit': 'шт'}),
    (2, {'name': 'Компьютер', 'price': 62000, 'quantity': 2, 'unit': 'шт'}),
    (3, {'name': 'Фен', 'price': 2000, 'quantity': 7, 'unit': 'шт'})
]
print(products)

i = 0
names = []
prices = []
quantities = []
units = []
while i < len(products):
    names.append(products[i][1]["name"])
    prices.append(products[i][1]['price'])
    quantities.append(products[i][1]['quantity'])
    units.append(products[i][1]['unit'])
    i += 1

summary = {"name": names, "price": prices, "quantities": quantities, "units": units}
print(summary)

products = []

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
    new = input("Чтобы ВЫЙТИ наберите '1', чтобы добавить еще товар введите любой символ: ")
    products.append(prod_tuple)

print("Текущая номенклатура товаров:\n", products)

names = []
prices = []
quantities = []
units = []
i = 0

while i < len(products):
    names.append(products[i][1]["name"])
    prices.append(products[i][1]['price'])
    quantities.append(products[i][1]['quantity'])
    units.append(products[i][1]['unit'])
    i += 1

summary = {"name": names, "price": prices, "quantities": quantities, "units": units}
print("Свод в разрезе характеристик:\n", summary)

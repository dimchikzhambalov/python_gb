# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

the_list = input("Введите через пробел значения вашего списка: ").split()
new_list = []
n = len(the_list)

if n % 2 == 0:
    list1 = the_list[::2]
    list2 = the_list[1::2]

    i = 0
    while i < len(list2):
        new_list.append(list2[i])
        new_list.append(list1[i])
        i += 1
else:
    list1 = the_list[:n-1:2]
    list2 = the_list[1:n-1:2]
    i = 0
    while i < len(list2):
        new_list.append(list2[i])
        new_list.append(list1[i])
        i += 1
    new_list.append(the_list[-1])

print("Вот ваш список:", the_list)
print("А вот он после обмена значениями:", new_list)

n = int(input("Введите целое положительное число: "))
max_num = n % 10

while n > 9:
    if max_num == 9:
        break
    n = n // 10
    num = n % 10
    if num > max_num:
        max_num = num

print(f"Максимальная цифра в числе: {max_num}")

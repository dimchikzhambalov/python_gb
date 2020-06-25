try:
    with open(f"text_5.txt", "w+", encoding="utf-8") as f_obj:
        try:
            text = input("Введите числа через пробел: ").split()
            f_obj.writelines(text)
            nums = []
            for num in text:
                num = int(num)
                nums.append(num)
            print(f"Сумма введенных чисел составляет: {sum(nums)}")
        except ValueError:
            print("Необходимо вводить числа через пробел")
except IOError:
    print("Error")

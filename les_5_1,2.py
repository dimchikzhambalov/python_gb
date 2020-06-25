# filename = input("Введите имя файла: ")
try:
    with open(f"text_1.txt", "w+", encoding="utf-8") as f_obj:
        while True:
            text = input("Введите текст (для выхода: пустая строка + Enter): ")
            if len(text) > 0:
                f_obj.writelines([text, "\n"])
            else:
                break
        f_obj.seek(0)
        print(f_obj.read())
        lines = 0
        wil = []
        f_obj.seek(0)
        for line in f_obj:
            if len(line) > 1:
                lines += 1
                words = len(line.split())
            wil.append(words)
        print(f"В файле {lines} не пустых строк")
        n = 1
        for i in wil:
            print(f"Строка {n} cодержит {i} слов/-о/-а.")
            n += 1
except IOError:
    print(IOError)

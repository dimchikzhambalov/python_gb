try:
    with open("text_3.txt",  encoding="utf-8") as f_obj:
        try:
            empls = {}
            for rec in f_obj:
                empl = rec.split()
                empls.update({empl[0]: float(empl[1])})
            less20k = []
            sal = []
            for name in empls.keys():
                if empls.get(name) < 20000:
                    less20k.append(name)
            print("Сотрудники с окладом менее 20 000 руб.:")
            for i in less20k:
                print("\t", i)
            print("Средняя величина дохода: ", sum(empls.values())/len(empls.values()))
        except ValueError:
            print("Формат данных в файле: {Фамилия}{Пробел}{Сумма цифрами}")
except IOError:
    print("Error")

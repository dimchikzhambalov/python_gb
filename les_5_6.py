try:
    with open("text_6.txt", encoding="utf-8") as f_obj:
        try:
            subj = []
            lect = []
            pract = []
            labor = []
            for line in f_obj:
                my_list = line.split(" ")
                subj.append(my_list[0][0:-1])
                lect_t = []
                pract_t = []
                labor_t = []
                for i in list(my_list[1]):
                    if i.isdigit():
                        lect_t.append(i)
                for i in list(my_list[2]):
                    if i.isdigit():
                        pract_t.append(i)
                for i in list(my_list[3]):
                    if i.isdigit():
                        labor_t.append(i)
                lect.append(''.join(lect_t))
                pract.append(''.join(pract_t))
                labor.append(''.join(labor_t))
            table = {}
            for i in subj:
                cnt = 0
                if lect[subj.index(i)].isdigit():
                    cnt += int(lect[subj.index(i)])
                if pract[subj.index(i)].isdigit():
                    cnt += int(pract[subj.index(i)])
                if labor[subj.index(i)].isdigit():
                    cnt += int(labor[subj.index(i)])
                table.update({i: cnt})
            print(table)
        except ValueError:
            print("Ошибка в данных")
except IOError:
    print("Error")

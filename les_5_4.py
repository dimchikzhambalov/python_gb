my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    with open("text_4.txt", encoding="utf-8") as f_obj:
        with open("text_4.1.txt", "w", encoding="utf-8") as tf_obj:
            for line in f_obj:
                w = line.split()
                eng = w[0]
                rus = my_dict.get(eng)
                w.pop(0)
                w.insert(0, rus)
                w.append("\n")
                tf_obj.writelines(w)
except IOError:
    print("Error")

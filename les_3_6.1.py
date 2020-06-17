"""
На входе слово на латинице с маленькой буквы.
Выводим исходное слово с заглавной буквы
"""


def int_func(word):
    case = chr(ord(word[0]) - 32)
    word.pop(0)
    word.insert(0, case)
    return ''.join(word)


text = list(input("Введите слово на латинице маленькими буквами: "))
print(int_func(text))

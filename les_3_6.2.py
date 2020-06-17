"""
На входе строка из нескольких слов на латинице через пробел с маленькой буквы.
Выводим исходную строку в которой каждое слово с заглавной буквы
"""
def int_func(word):
    case = chr(ord(word[0]) - 32)
    word.pop(0)
    word.insert(0, case)
    return ''.join(word)


text = input("Введите несколько слов на латинице маленькими буквами: ").split()
output = []
for i in text:
    output.append(int_func(list(i)))

print(' '.join(output))

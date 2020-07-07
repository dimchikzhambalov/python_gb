class Date:
    def __init__(self, date_str):
        self.date_str = date_str
        if (date_str[2] or date_str[5]) != "-" or len(date_str) > 10:
            print(f"Дата введена не по формату, ожидается дата в формате: 'ДД-ММ-ГГГГ'")

    @classmethod
    def mode(cls, date_str):
        day = int(date_str[0:2])
        month = int(date_str[3:5])
        year = int(date_str[6:10])
        return f"День: {day:02d}, Месяц: {month:02d}, Год: {year:04d}"

    @staticmethod
    def val(date_str):
        day = int(date_str[0:2])
        month = int(date_str[3:5])
        year = int(date_str[6:10])
        if month > 12 or month < 1:
            return f"Месяц может иметь значение от 1 до 12, вы ввели {int(date_str[3:5])}"
        elif (day > 30 or day < 1) and month not in [1, 2, 3, 5, 7, 8, 10, 12]:
            return f"Для указанного месяца день может иметь значение от 1 до 30, вы ввели {int(date_str[0:2])}"
        elif (day > 31 or day < 1) and month in [1, 3, 5, 7, 8, 10, 12]:
            return f"Для указанного месяца день может иметь значение от 1 до 31, вы ввели {int(date_str[0:2])}"
        elif (day > 29 or day < 1) and month == 2:
            return f"Для указанного месяца день может иметь значение от 1 до 29, вы ввели {int(date_str[0:2])}"
        elif year > 2099:
            return "Так далеко в будущее мы еще не заглядывали"
        elif year < 1900:
            return "Там все пылью покрылось. Зачем тебе это?"
        else:
            return date_str


print(Date.mode("20-02-2020"))
print(Date.val("30-02-2200"))
print(Date.val("45-12-2200"))
print(Date.val("31-11-2200"))
print(Date.val("31-13-2200"))
print(Date.val("31-12-1800"))
print(Date.val("31-12-2200"))

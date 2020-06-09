print("Закончился очередной отчетный период.")
print("Давайте подведем его итоги.")

rev = float(input("Сумма выручки: "))
cst = float(input("Сумма издержек: "))

if rev == cst:
    print("К счастью мы не в убытке, но и прибыли мы не получили...")
elif cst > rev:
    loss = cst - rev
    print(f"К сожалению мы получили убытки в размере: {loss} руб.")
else:
    empl_cnt = int(input("Какое кол-во сотрудников в фирме: "))
    prof = rev - cst
    rent = prof / rev * 100
    print("Мы получили прибыль в размере %.2f руб., рентабельность составила %d процентов." % (prof, rent))
    prof_per_empl = prof / empl_cnt
    print("Прибыль на одного сотрудника составила %.2f руб." % prof_per_empl)

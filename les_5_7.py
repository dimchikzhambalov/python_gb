import json

try:
    with open(f"text_7.txt", encoding="utf-8") as f_obj:
        try:
            profit = {}
            for line in f_obj:
                company_in = line.split()
                amount = 0
                if company_in[2].isdigit():
                    amount += int(company_in[2])
                if company_in[3].isdigit():
                    amount -= int(company_in[3])
                profit.update({company_in[0]: amount})
            profit_amt = 0
            cnt = 0
            for i in profit.values():
                if i > 0:
                    profit_amt += i
                    cnt += 1
            avg_profit = profit_amt / cnt
            summary = [profit, {"average_profit": avg_profit}]
            print(summary)
        except ValueError:
            print("Ошибка в данных")
        with open("text_77.json.", "w+", encoding="utf-8") as j_obj:
            json.dump(summary, j_obj)
except IOError:
    print("Error")

age = int(input("Введите возраст: "))
dohod = int(input("Введите ежемесячный доход: "))
kredit = int(input("Введите размер кредита: "))
time = int(input("Введите срок кредита: "))
credit_history = input("Кредитная история: отличная/хорошая/удовлетворительная/плохая: ")
poruch = input("Поручители: да/нет: ")
zalog = input("Залог: да/нет: ")

kredit_dohod = kredit / dohod

poruch = True if poruch.lower() == "да" else False
zalog = True if zalog.lower() == "да" else False

risk_ball = int(0)

if dohod <= 2222:
    risk_ball += 2

else:
    risk_ball += 1

if poruch == False:
    risk_ball += 1

if zalog == False:
    risk_ball += 1

if age >= 62 or age <= 21:
    print("Кредит не одобрен из-за возраста")
    exit()

if credit_history.lower() == "удовлетворительная":
    risk_ball += 1

if credit_history.lower() == "плохая":
    risk_ball += 2

if kredit <= 20000:
    print("Процентная ставка: 7%")

elif 20000 < kredit <= 35000:
    print("Процентная ставка: 9%")
    risk_ball += 1

else:
    print("Процентная ставка: 11%")
    risk_ball += 2

if 6 <= risk_ball == 8:
    print("Критический риск")

elif 3 <= risk_ball < 6:
    print("Высокий риск")

elif 1 <= risk_ball < 3:
    print("Средний риск")

elif risk_ball == 0:
    print("Низкий риск")

if risk_ball < 6:
    print("Кредит одобрен")

else:
    print("Кредит не одобрен")
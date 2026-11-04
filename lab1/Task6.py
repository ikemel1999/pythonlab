day = int(input("День: "))
month = int(input("Месяц: "))

if month < 10:
    print(f"Дата: {day}.0{month}")
else:
    print(f"Дата: {day}.{month}")

if (day <= 19 and month == 1) or ( day >= 22 and month == 12):
    print("козерог")

elif (day >= 20 and month == 1) or (day <= 18 and month == 2):
    print("Водолей")

elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
    print("Рыбы")

elif (day >= 21 and month == 3) or (day <= 19 and month == 4):
    print("Овен")

elif (day >= 20 and month == 4) or (day <= 20 and month == 5):
    print("Телец")

elif (day >= 21 and month == 5) or (day <= 20 and month == 6):
    print("Близнецы")

elif (day >= 21 and month == 6) or (day <= 22 and month == 7):
    print("Рак")

elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
    print("Лев")

elif (day >= 23 and month == 8) or (day <= 22 and month == 9):
    print("Дева")

elif (day >= 23 and month == 9) or (day <= 22 and month == 10):
    print("Весы")

elif (day >= 23 and month == 10) or (day <= 21 and month == 11):
    print("Скорпион")

elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
    print("Стрелец")
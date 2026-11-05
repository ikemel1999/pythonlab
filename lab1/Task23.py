dohod = float(input("Введите доход: "))
zhile = float(input("Введите расходы на жилье: "))
eda = float(input("Введите расходы на питание: "))
transport = float(input("Введите расходы на транспорт: "))
razvlechenia = float(input("Введите расходы на развлечения: "))
podushka = float(input("Сколько откладываете на черный день: "))

max_zhile = dohod * 0.3
max_eda = dohod * 0.2
max_transport = dohod * 0.1
max_razvlechenia = dohod * 0.1
min_podushka = dohod * 0.25

summa = zhile + eda + transport + razvlechenia + podushka
print(f"Ваши траты: {summa} денег")

if dohod <= summa:
    print(f"Нужно полностью пересмотреть траты и где-то найти: {(summa - dohod)} денег")

if zhile > max_zhile:
    print(f"Нужно жилье дешевле хотя бы на {(zhile - max_zhile)} денег")

if eda > max_eda:
    print(f"Нужно есть максимум на {max_eda} денег")

if transport > max_transport:
    print(f"Нужно больше передвигаться пешком и тратить на транспорт на {(transport - max_transport)} денег меньше ")

if razvlechenia > max_razvlechenia:
    print(f"Нужно развлекать себя дешевле, максимум за {max_razvlechenia} денег в месяц")

if podushka < min_podushka:
    print(f"Нужно больше откладывать, при вашем доходе можно откладвать на {(min_podushka - podushka)} денег больше")

else:
    print("Вы молодец и делаете все правильно!!!")
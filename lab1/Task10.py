age = int(input("Введите возраст: "))
vip = input("ВИП да/нет: ")
hb = input("ДР да/нет: ")
summa = int(input("Введите сумму: "))

vip = True if vip.lower() == "да" else False
hb = True if hb.lower() == "да" else False

itog_summa = int(0)
skidka = int(0)

if summa > 1000 and vip == False:
    skidka += 10

if hb == True:
    skidka += 5

if age >= 63:
    skidka += 5

if vip == True:
    skidka += 15

itog_summa = summa - (summa * skidka / 100)

print(f"Итоговая скидка: {skidka}\nИтоговая сумма: {itog_summa}")
minutes = int(input("Введите кол-во минут: "))
sms = int(input("Введите кол-во сообщений: "))
internet = int(input("Введите кол-во израсходованных мб памяти: "))
summa = 24.99
if minutes > 60:
    pr_min = 0.89 * (minutes - 60)
    print(f" Сумма за доп минуты: {pr_min:.2f}")
    summa += pr_min

if sms > 30:
    pr_sms = 0.59 * (sms - 30)
    print(f" Сумма за доп смс: {pr_sms:.2f}")
    summa += pr_sms

if internet > 1000:
    pr_int = 0.79 * (internet - 1000)
    print(f" Сумма за доп интернет: {pr_int:.2f}")
    summa += pr_int

summa = summa * 1.02
tax = summa * 0.02
print(f" Налог: {tax:.2f}\n базовая сумма тарификации: 24.99")

print(f" Сумма к оплате: {summa:.2f}")
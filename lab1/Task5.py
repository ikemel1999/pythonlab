a = int(input("введите первое число: "))
b = int(input("введите второе число: "))

print(f" summa = {a + b}\n raznost = {a - b}\n ptoizvedenie = {a * b}\n stepen = {a ** b}\n")

if b == 0:
    print(" Деление на 0 запрещено")
else:
    print(f" chastnoe = {a / b}\n ostatok = {a % b}")
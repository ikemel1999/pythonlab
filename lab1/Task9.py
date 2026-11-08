mm = 0.001
cm = 0.01
m = 1
km = 1000

mg = 0.001
g = 1
kg = 1000
t = 1000000

sek = 1
minuta = 60

vvod1 = input("Введите что переводим: ")
vvod2 = input("Введите во что переводим: ")
vvod3 = int(input("Введите значение: "))

if vvod1 == "mm":    
    a = mm
elif vvod1 == "cm":
    a = cm
elif vvod1 == "m":
    a = m
elif vvod1 == "km":
    a = km
elif vvod1 == "mg":
    a = mg
elif vvod1 == "g":
    a = g
elif vvod1 == "kg":
    a = kg
elif vvod1 == "t":
    a = t
elif vvod1 == "sek":
    a = sek
elif vvod1 == "minuta":
    a = minuta

if vvod2 == "mm":    
    b = mm
elif vvod2 == "cm":
    b = cm
elif vvod2 == "m":
    b = m
elif vvod2 == "km":
    b = km
elif vvod2  == "mg":
    b = mg
elif vvod2  == "g":
    b = g
elif vvod2  == "kg":
    b = kg
elif vvod2  == "t":
    b = t
elif vvod2  == "sek":
    b = sek
elif vvod2 == "minuta":
    b = minuta

result = vvod3 * a / b
print(f"Результат перевода: {result}")
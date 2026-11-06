txt = input("Введите текст: ")

txt = txt.replace("," , "").replace("." , "")

slova = txt.lower().split()

print(f"Список: {slova}")

print(f"Кол-во слов: {len(slova)}")

slovar = {}

for word in set(slova):
    chastota = slova.count(word)
    slovar[word] = chastota
    print(f"Частота слова {word}: {chastota} ")

samoe_chastoe = max(slovar, key = slovar.get)
print(f"Самое часто встречающееся слово: {samoe_chastoe}, встречается {slovar[samoe_chastoe]} раз")

long = max(slovar, key = len)
print(f"Самое длинное: {long}")

short = min(slovar, key = len)
print(f"Самое короткое: {short}")

filtr_slova = [word for word in slova if len(word) >= 3]
print(f"Новый список: {filtr_slova}, кол-во слов: {len(filtr_slova)}")
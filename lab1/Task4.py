string = input("Введите строку: ")
new_string = string[::-1]
if new_string == string:
    print("Палиндром")
else:
    print("не Палиндром")
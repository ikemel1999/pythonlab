import random

target = random.randint(1, 100)

while True:
    attemp = int(input("Введите число: "))
    if attemp < target:
        print("Загаданное число больше")
    elif attemp > target:
        print("Загаданное число меньше")
    elif attemp == target:
        print(f"Вы угадали, загаданное число: {attemp}")
        break
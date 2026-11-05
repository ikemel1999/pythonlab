txt = input("Введите числа: ").split()
nums = []
for num in txt:
    if float(num).is_integer():
        nums.append(int(float(num)))
    else:
        nums.append(float(num))
print(nums)
print(f"Уникальные числа: {set(nums)}")

povt_nums = []

for num in set(nums):
    chastota = nums.count(num)
    if chastota >= 2:
        povt_nums.append(num)

print(f"Повторяющиеся числа: {povt_nums}")

chet = []
nechet = []

for num in set(nums):
    if num % 2 == 0:
        chet.append(num)
    else:
        nechet.append(num)
print(f"Четные: {chet}, нечет: {nechet}")

negativ = []

for num in set(nums):
    if num < 0:
        negativ.append(num)
print(f"Отрицательные: {negativ}")

flot = []
for num in set(nums):
    if not num.is_integer():
        flot.append(num)
print(f"С плавающей точкей: {flot}")

print(f"Самое большое: {max(set(nums))}")
print(f"Самое маленькое: {min(set(nums))}")

five = []

for num in set(nums):
    if num % 5 == 0:
        five.append(num)

print(f"Сумма кратных 5: {sum(five)}")
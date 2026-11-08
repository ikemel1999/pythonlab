summa = int(input("введите сумму: "))
klvo100 = 0 
klvo50 = 0
klvo10 = 0
klvo5 = 0
klvo2 = 0
klvo1 = 0

klvo100 = summa // 100
summa = summa % 100

klvo50 = summa // 50
summa = summa % 50

klvo10 = summa // 10
summa = summa % 10

klvo5 = summa // 5
summa = summa % 5

klvo2 = summa // 2
summa = summa % 2

klvo1 = summa // 1
summa = summa % 1

print(f"количество купюр и монет определенного номинала: \n 100: {klvo100}\n 50: {klvo50}\n 10: {klvo10}\n 5: {klvo5}\n 2: {klvo2}\n 1: {klvo1}")
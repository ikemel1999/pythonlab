profucts = [
    {"name": "штаны", "price": 150, "sold" : 30},
    {"name": "куртка", "price": 250, "sold": 10},
    {"name": "кофта", "price": 100, "sold": 40},
    {"name": "майка", "price": 70, "sold": 33}
]

max_sum = 0
best_tovar = ""

for tovar in profucts:
    sum = tovar["price"] * tovar["sold"]
    print(f"{tovar["name"]} продано на сумму: {sum}")
    if sum > max_sum:
        max_sum = sum
        best_tovar = tovar["name"]

print(f"Самый прибыльный товар: {best_tovar}, сумма: {max_sum}")

uniq = []

for tovar in profucts:
    if tovar["name"] not in uniq:
        uniq.append(tovar["name"])

print(f"Кол-во уникальных наименованний: {len(uniq)}")
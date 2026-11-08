def cache(func):
    slovar = {}
    def wrapper(*args):
        if args in slovar:
            return slovar[args]
        else:
            slovar[args] = func(*args)
            return slovar[args]
    return wrapper

@cache
def summ(a, b):
    return a + b

print(f"Через функцию: {summ(3, 6)}")
print(f"Из кэша: {summ(3, 6)}")

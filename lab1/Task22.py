def type_check(*types):
    def decorator(func):
        def wrapper(*args):
         for i in range(len(args)):
            if not isinstance(args[i], int):
               raise TypeError(f"{args[i]} не того типа")
         return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def summa(a, b):
    return a + b

print(f"Сумма: {summa(3, 6)}")
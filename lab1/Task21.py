import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        result_time = (end - start) * 1000
        print(f"Время выполнения: {result_time} мс")
        return result
    return wrapper

@timing
def summa(a, b):
    return a + b

print(f"Сумма: {summa(3, 6)}")
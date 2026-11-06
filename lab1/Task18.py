import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        file = open("text.txt", 'w')
        file.write(f"Time: {time.strftime("%Y-%m-%d %H:%M:%S")} ")
        file.write(f"Name: {func.__name__} ")
        file.write(f"Arg: {args}, {kwargs}")
        file.close()
        return func(*args, **kwargs)
    return wrapper

@log_calls
def func(txt):
    print(txt)

func("Privet kak dela")
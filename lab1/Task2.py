password = input("Введите пароль: ")
if len(password) < 16:
    print(f"Слишком короткий")
elif password.isalpha() or password.isdigit():
    print(f"Слабый пароль")
else:
    print(f"Надежный пароль")
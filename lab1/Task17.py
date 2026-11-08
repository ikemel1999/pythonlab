dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}


def func(dict_1, dict_2):
    for key, znach in dict_2.items():
        if key in dict_1 and isinstance(dict_1[key], dict) and isinstance(znach, dict):
            func(dict_1[key], dict_2[key])
        else:
            dict_1[key] = znach

func(dict_a, dict_b)

print(dict_a)
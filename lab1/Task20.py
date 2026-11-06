def flatt_list(list_0):
    a = 0
    while a < len(list_0):
        now = list_0[a]
        if isinstance(now, list):
            flatt_list(now)
            now = [num for num in now if num not in list_0]
            list_0[a:a+1] = now

            a += len(now) 

        else:
            a += 1

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]] 

flatt_list(list_a)

print(list_a)

            
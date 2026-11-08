txt1 = input("Введите числа 1: ").split()
txt2 = input("Введите числа 2: ").split()
nums1 = []
for num in txt1:
    if float(num).is_integer():
        nums1.append(int(float(num)))
    else:
        nums1.append(float(num))

nums2 = []
for num in txt2:
    if float(num).is_integer():
        nums2.append(int(float(num)))
    else:
        nums2.append(float(num))

print(f"Числа в 2 списках одновременно: {set(nums1) & set(nums2)}")
print(f"Числа только в первом списке: {set(nums1) - set(nums2)}")
print(f"Числа только во втором списке: {set(nums2) - set(nums1)}")
print(f"Числа в 2 списках одновременно: {set(nums1) ^ set(nums2)}")
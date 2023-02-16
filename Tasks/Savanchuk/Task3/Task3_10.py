num = input("Введите числа:\n")
num = num.split()
max = 0
list = []
for i in num:
    if (int(i) % 2 != 0 and int(i) % 3 !=0 and int(i) !=1) or int(i) == 2 or int(i) == 3:
        list.append(i)
for i in list:
    if int(i) > max:
        max = int(i)
print(max)        
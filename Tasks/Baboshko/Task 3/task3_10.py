int_list = input('Пожалуйста, введите любое количество чисел: \n').split()
for i in range(len(int_list)):
    total, max = 0, 0
    for j in range(1, int(int_list[i])+1):
        if int(int_list[i]) % j == 0:
            total += 1
    if total == 2 and int(int_list[i]) > max:
        max = int(int_list[i])
print(max)
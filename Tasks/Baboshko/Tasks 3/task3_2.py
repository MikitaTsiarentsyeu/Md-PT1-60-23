int_list = input('Пожалуйста, введите список чисел через пробел: \n').split()
total = 0
for i in range(len(int_list)):
    if int_list[i].isdigit() and int(int_list[i]) % 2 == 0:
        total += int(int_list[i])
print(total)







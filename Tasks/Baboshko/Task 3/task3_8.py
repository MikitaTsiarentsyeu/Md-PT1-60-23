int_list = input('Пожалуйста, введите любое количество чисел: \n').split()
sum = 0
for i in range(len(int_list)):
    if int_list[i].isdigit():
        sum += int(int_list[i])
print('Среднее арифметическое списка чисел:', sum / len(int_list))

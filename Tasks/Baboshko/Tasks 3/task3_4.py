new_numbers = input('введите любое количество чисел, пожалуйста: \n').split()
max, max_2= int(new_numbers[0]), 0
for i in range(1, len(new_numbers)):
    if int(new_numbers[i]) >= max:
        max, max_2 = int(new_numbers[i]), max
print(max_2)
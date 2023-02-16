your_list = input('Enter numbers separated by spaces:\n').split()
num_list = [int(i) for i in your_list]

if num_list[0] < num_list[1]:
    number_1, number_2 = num_list[0], num_list[1]
else:
    number_1, number_2 = num_list[1], num_list[0]

for number in num_list[2:]:
    if number < number_1:
        number_2, number_1 = number_1, number
    elif number_1 < number < number_2:
        number_2 = number
    else:
        continue

print(number_2)
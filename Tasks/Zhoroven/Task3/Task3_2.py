number = input('Enter some numbers, for example:"3 44 88 ...":\n')

number_list = list(number.split(' '))
print(number_list)

summa = 0

for i in number_list:
    summa += int(i)

print(f"Sum of numbers {summa}")

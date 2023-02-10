def average(lst: list):
    return sum(lst) / len(lst)
n = int(input('N: '))
lst = []
for i in range(n):
    print(f'Введи {i}-й элемент: ')
    lst.append(float(input()))
 
aver = average(lst)
print(f'Среднее арифметическое: {aver}')

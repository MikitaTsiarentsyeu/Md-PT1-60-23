print('Рассчитайте вашу прибыль от вклада.\nВведите сумму депозита в рублях')
print('a=', end= ' ')
a = input()
while (a.isdigit()==0):
       print('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
       print('a=', end= ' ')
       a = input()
a=int(a)
   
print('Введите количество месяцев')
print('b=', end= ' ')
b = input()
while (b.isdigit()==0):
       print('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
       print('b=', end= ' ')
       b = input()
b=int(b)
       
print('Введите желаемый процент годовых')
print('с=', end= ' ')
c = input()
while (c.isdigit()==0):
       print('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
       print('c=', end= ' ')
       c = input()
c=int(c)
c=c/12


for i in range (b):

    a = a*(c/100+1)
    
    print(f'Сумма вашего вклада за {i+1} месяц {round(a,2)} рублей\n')


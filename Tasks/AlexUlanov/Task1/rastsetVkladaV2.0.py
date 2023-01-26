def beSureIsDigit():
     global x  
     x = input()
     while x.isdigit()==0:
               print('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
               x = input()
               if x.isdigit()==1:
                   break
              
print('Рассчитайте вашу прибыль от вклада.\nВведите сумму депозита в рублях')
print('a=', end= ' ')
beSureIsDigit()
a = int(x)

   
print('Введите количество месяцев')
print('b=', end= ' ')
beSureIsDigit()
b = int(x)

       
print('Введите желаемый процент годовых')
print('с=', end= ' ')
beSureIsDigit()
c = int(x)
c=c/12


for i in range (b):

    a = a*(c/100+1)
    
    print(f'Сумма вашего вклада за {i+1} месяц {round(a,2)} рублей\n')
    

       

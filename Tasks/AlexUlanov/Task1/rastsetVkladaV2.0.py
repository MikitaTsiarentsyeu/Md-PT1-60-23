def beSureIsDigit():
     global x  
     x = input()
     while x.isdigit()==0:
               x = input('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
               if x.isdigit()==1:
                   break
              
print('Рассчитайте вашу прибыль от вклада.\nВведите сумму депозита в рублях\na=', end= ' ')
beSureIsDigit()
a = int(x)

   
print('Введите количество месяцев\nb=', end= ' ')
beSureIsDigit()
b = int(x)

       
print('Введите желаемый процент годовых\nс=', end= ' ')
beSureIsDigit()
c = int(x)
c=c/12


for i in range (b):

    a = a*(c/100+1)
    
    print(f'Сумма вашего вклада за {i+1} месяц {round(a,2)} рублей\n')
    

       

def beSureIsDigit():
    global x  
    x = input()
    check = x.find(".")
    flag = False
    while flag != True:
            for i in range (len(x)):
                if (x[i].isdigit()==1 or (check==i and (len(x)>2))):
                    flag = True
                    continue
                else:
                    flag = False
                    x = input('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
                    check = x.find(".")
                    break
                if x == y:
                    x = input('ВЫ ВВЕЛИ СИМВОЛ А НЕ ЧИСЛО!!!ВВОДИТЕ ЗАНОВО!!!\n')
                    check = x.find(".")
                    break
              
print('Рассчитайте вашу прибыль от вклада.\nВведите сумму депозита в рублях\na=', end= ' ')
beSureIsDigit()
a = float(x)

   
print('Введите количество месяцев\nb=', end= ' ')
beSureIsDigit()
b = int(x)

       
print('Введите желаемый процент годовых\nс=', end= ' ')
beSureIsDigit()
c = float(x)
c=c/12


for i in range (b):

    a = a*(c/100+1)
    
    print(f'Сумма вашего вклада за {i+1} месяц {round(a,2)} рублей\n')
    


import datetime
first_dict = { 1 : 'Один' ,2 : 'Два' , 3 : 'Три' , 
          4 : 'Четыре', 5 : 'Пять' , 6 : 'Шесть' ,
          7 : 'Семь' , 8 : 'Восемь', 9 : 'Девять' ,
          10 : 'Десять' , 11 : 'Одиннадцать' , 12 : 'Двeнадцать', 0 : 'Двенадцать' }
second_dict = {1 : 'Первого' ,2 : 'Второго' , 3 : 'Третьего' , 
          4 : 'Четвертого', 5 : 'Пятого' , 6 : 'Шестого' ,
          7 : 'Седьмого' , 8 : 'Восьмого', 9 : 'Девятого' ,
          10 : 'Десятого' , 11 : 'Одиннадцатого' , 12 : 'Двeнадцатого', 0 : 'Двенадцатого'}
third_dict = { 1 : 'Одна' ,2 : 'Две' , 3 : 'Три' , 
          4 : 'Четыре', 5 : 'Пять' , 6 : 'Шесть' ,
          7 : 'Семь' , 8 : 'Восемь', 9 : 'Девять' ,
          10 : 'Десять' , 11 : 'Одиннадцать' , 12 : 'Двeнадцать',
          13 : 'Тринадцать' , 14 : 'Четырнадцать', 15 : 'Пятнадцать',
          16 : 'Шестнадцать', 17 : 'Семнадцать', 18 : 'Восемнадцать',
          19 : 'Девятнадцать', 20 : 'Двадцать' , 21: 'Двадцать одна',
          22: 'Двадцать две', 23 : 'Двадцать три', 24 : 'Двадцать четыре',
          25: 'Двадцать пять', 26 : 'Двадцать шесть', 27 : 'Двадцать семь',
          28: 'Двадцать восемь', 29: 'Двадцать девять',31 : 'Тридцать одна',
          32 : 'Тридцать две',33 : 'Тридцать три',34 : 'Тридцать четыре',
          35 : 'Тридцать пять',36 : 'Тридцать шесть',37 : 'Тридцать семь',
          38 : 'Тридцать восемь',39 : 'Тридцать девять',40 : 'сорок',
          41 : 'Сорок одна',42 : 'Сорок две',43 : 'Сорок три',
          44 : 'Сорок четыре', 45 : 'Сорок пять', 46 : 'Сорок шесть',
          47 : 'Сорок семь',48 : 'Сорок восемь',49 : 'Сорок девять',
          50 : 'Пятьдесят', 51 : 'Пятьдесят одна', 52 : 'Пятьдесят две',
          53 : 'Пятьдесят три',54 : 'Пятьдесят четыре',55 : 'Пятьдесят пять',
          56 : 'Пятьдесят шесть',57 : 'Пятьдесят семь',58 : 'Пятьдесят восемь',
          59 : 'Пятьдесят девять'}
fourth_dict = { 1 : 'одной', 2 : 'двух', 3 : 'трех', 4: 'четырех', 5: 'Пяти',
                6 : 'шести', 7 : 'семи',8 : 'восьми',9 : 'девяти',10 : 'десяти',
                11 : 'одиннадцати',12 : 'двенадцати',13 : 'тренадцати',
                14 : 'четырнадцати', 15 : ' пятнадцати'}
print('Добрый день,вы хотите узнать сколько времени?')
time_question = float(input('Для текстового вывода текущего времени - Введите "1"\nДля текстового вывода введеного времени - Введите "2"\n')) 
if time_question == 1:
    time = datetime.datetime.now()
    hourse = time.hour
    minutes = time.minute
    hourse_2 = hourse - 12
    count_hourse_1 = hourse_2 + 1
    count_hourse_2 = hourse + 1
    count_for_min = 60 - minutes
     #min == 0
    if minutes == 0 and hourse >= 1 and  hourse <= 12:
        if hourse >= 5 and hourse <= 12 :
            print(first_dict[hourse], 'часов ровно')
        elif hourse >= 2 and hourse <= 4:
            print(first_dict[hourse], 'часа ровно')
        elif hourse == 1:
            print(first_dict[hourse], 'час ровно')
    elif minutes == 0 and hourse >= 13:
        if hourse >= 17 and hourse <= 24:
            print(first_dict[hourse_2], 'часов ровно')
        elif hourse >= 14 and hourse <= 16:
            print(first_dict[hourse_2], 'часа ровно')
        elif hourse == 13:
            print(first_dict[hourse_2], 'час ровно')
    elif minutes == 0 and hourse == 00:
        print(first_dict[hourse], 'часов ровно')
     #min == 30
    elif minutes == 30 and hourse >= 12 and hourse <= 24:
        print('Половина',second_dict[count_hourse_1])
    elif minutes == 30 and hourse <= 11 and hourse >= 1:
        print('Половина',second_dict[count_hourse_2]) 
    elif minutes == 30 and hourse == 0:
        print('Половина',second_dict[count_hourse_2])
     #min < 30
    elif minutes < 30 and hourse >= 12 and hourse <= 24  :
        if (minutes >= 2 and minutes<=4) or (minutes>=22 and minutes <= 24):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_1])
        elif (minutes >= 5 and minutes <= 21) or (minutes >= 25 and minutes <= 29):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_1])
        elif minutes == 1:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_1])
    elif minutes < 30 and hourse<= 11 and hourse >=1 :
        if (minutes >= 2 and minutes<=4) or (minutes>=22 and minutes <= 24):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 5 and minutes <= 21) or (minutes >= 25 and minutes <= 29):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 1:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2])
    elif minutes < 30 and hourse == 0:
        if (minutes >= 2 and minutes<=4) or (minutes>=22 and minutes <= 24):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 5 and minutes <= 21) or (minutes >= 25 and minutes <= 29):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 1:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2]) 
     #min > 30 and min < 45   
    elif minutes > 30 and minutes < 45 and hourse >=12 and hourse <=24 :
        if (minutes >= 32 and minutes <= 34) or (minutes >= 42 and minutes<= 44):
            print(third_dict[minutes],'минуты',second_dict[count_hourse_1])
        elif (minutes >= 35 and minutes <= 40):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_1])
        elif minutes == 31 or minutes == 41:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_1])
    elif minutes > 30 and minutes < 45 and hourse<= 11 and hourse >=1 :
        if (minutes >= 32 and minutes<=34) or (minutes>=42 and minutes <= 44):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 35 and minutes <= 40) :
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 31 or minutes == 41:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2])
    elif minutes > 30 and minutes < 45 and hourse == 0:
        if (minutes >= 32 and minutes<=34) or (minutes>=42 and minutes <= 44):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 35 and minutes <= 40) :
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 31 or minutes == 41:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2])
    # min >= 45
    elif minutes >= 45 and hourse >= 12 and hourse <=24:
        if minutes >= 45 and minutes <= 58:
            print('Без',fourth_dict[count_for_min], 'минут',first_dict[count_hourse_1] )
        elif minutes == 59:
            print('Без',fourth_dict[count_for_min], 'минуты',first_dict[count_hourse_1] )
    elif minutes >= 45 and hourse >= 1 and hourse <=11:
        if minutes >= 45 and minutes <= 58:
            print('Без',fourth_dict[count_for_min], 'минут',first_dict[count_hourse_2] )
        elif minutes == 59:
            print('Без',fourth_dict[count_for_min], 'минуты',first_dict[count_hourse_2] )






elif time_question == 2:
    time_format = input('Введите время в формате "чч.мм"\n')
    time_format = time_format.split('.')
    hourse = int(time_format[0])
    minutes = int(time_format[1])
    hourse_2 = hourse - 12
    count_hourse_1 = hourse_2 + 1
    count_hourse_2 = hourse + 1
    count_for_min = 60 - minutes
     #min == 0
    if minutes == 0 and hourse >= 1 and  hourse <= 12:
        if hourse >= 5 and hourse <= 12 :
            print(first_dict[hourse], 'часов ровно')
        elif hourse >= 2 and hourse <= 4:
            print(first_dict[hourse], 'часа ровно')
        elif hourse == 1:
            print(first_dict[hourse], 'час ровно')
    elif minutes == 0 and hourse >= 13:
        if hourse >= 17 and hourse <= 24:
            print(first_dict[hourse_2], 'часов ровно')
        elif hourse >= 14 and hourse <= 16:
            print(first_dict[hourse_2], 'часа ровно')
        elif hourse == 13:
            print(first_dict[hourse_2], 'час ровно')
    elif minutes == 0 and hourse == 00:
        print(first_dict[hourse], 'часов ровно')
     #min == 30
    elif minutes == 30 and hourse >= 12 and hourse <= 24:
        print('Половина',second_dict[count_hourse_1])
    elif minutes == 30 and hourse <= 11 and hourse >= 1:
        print('Половина',second_dict[count_hourse_2]) 
    elif minutes == 30 and hourse == 0:
        print('Половина',second_dict[count_hourse_2])
     #min < 30
    elif minutes < 30 and hourse >= 12 and hourse <= 24  :
        if (minutes >= 2 and minutes<=4) or (minutes>=22 and minutes <= 24):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_1])
        elif (minutes >= 5 and minutes <= 21) or (minutes >= 25 and minutes <= 29):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_1])
        elif minutes == 1:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_1])
    elif minutes < 30 and hourse<= 11 and hourse >=1 :
        if (minutes >= 2 and minutes<=4) or (minutes>=22 and minutes <= 24):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 5 and minutes <= 21) or (minutes >= 25 and minutes <= 29):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 1:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2])
    elif minutes < 30 and hourse == 0:
        if (minutes >= 2 and minutes<=4) or (minutes>=22 and minutes <= 24):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 5 and minutes <= 21) or (minutes >= 25 and minutes <= 29):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 1:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2]) 
     #min > 30 and min < 45   
    elif minutes > 30 and minutes < 45 and hourse >=12 and hourse <=24 :
        if (minutes >= 32 and minutes <= 34) or (minutes >= 42 and minutes<= 44):
            print(third_dict[minutes],'минуты',second_dict[count_hourse_1])
        elif (minutes >= 35 and minutes <= 40):
            print(third_dict[minutes], 'минут', second_dict[count_hourse_1])
        elif minutes == 31 or minutes == 41:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_1])
    elif minutes > 30 and minutes < 45 and hourse<= 11 and hourse >=1 :
        if (minutes >= 32 and minutes<=34) or (minutes>=42 and minutes <= 44):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 35 and minutes <= 40) :
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 31 or minutes == 41:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2])
    elif minutes > 30 and minutes < 45 and hourse == 0:
        if (minutes >= 32 and minutes<=34) or (minutes>=42 and minutes <= 44):
            print(third_dict[minutes], 'минуты', second_dict[count_hourse_2])
        elif (minutes >= 35 and minutes <= 40) :
            print(third_dict[minutes], 'минут', second_dict[count_hourse_2])
        elif minutes == 31 or minutes == 41:
            print(third_dict[minutes], 'минута', second_dict[count_hourse_2])
    # min >= 45
    elif minutes >= 45 and hourse >= 12 and hourse <=24:
        if minutes >= 45 and minutes <= 58:
            print('Без',fourth_dict[count_for_min], 'минут',first_dict[count_hourse_1] )
        elif minutes == 59:
            print('Без',fourth_dict[count_for_min], 'минуты',first_dict[count_hourse_1] )
    elif minutes >= 45 and hourse >= 1 and hourse <=11:
        if minutes >= 45 and minutes <= 58:
            print('Без',fourth_dict[count_for_min], 'минут',first_dict[count_hourse_2] )
        elif minutes == 59:
            print('Без',fourth_dict[count_for_min], 'минуты',first_dict[count_hourse_2] )
    else:
        print('Введен неправильный формат')
else:
    print('Введите "1" или "2"')
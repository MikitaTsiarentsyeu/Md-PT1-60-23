import datetime

hour = {1:'один час', 2:'два часа', 3:'три часа',4:'четыре часа',5:'пять часов',
        6:'шесть часов',7:'семь часов',8:'восемь часов',9:'девять часов',10:'десять часов',
        11:'одиннадцать часов',12:'двенадцать часов', 0:'двенадцать часов'}

min = {1:'одна минута', 2:'две минуты', 3:'три минуты',4:'четыре минуты',5:'пять минут',
        6:'шесть минут',7:'семь минут',8:'восемь минут',9:'девять минут',10:'десять минут',
        11:'одиннадцать минут',12:'двенадцать минут',13:'тринадцать минут',14:'четырнадцать минут',
        15:'пятнадцать минут',16:'шестнадцать минут',17:'семнадцать минут',18:'восемнадцать минут',
        19:'девятнадцать минут',20:'двадцать минут',21:'двадцать одна минута',22:'двадцать две минуты',
        23:'двадцать три минуты',24:'двадцать четыре минуты',25:'двадцать пять минут',
        26:'двадцать шесть минут',27:'двадцать семь минут',28:'двадцать восемь минут',
        29:'двадцать девять минут',31:'тридцать одна минута',32:'тридцать две минуты',
        33:'тридцать три минуты',34:'тридцать четыре минуты',35:'тридцать пять минут',
        36:'тридцать шесть минут',37:'тридцать семь минут',38:'тридцать восемь минут',
        39:'тридцать девять минут',40:'сорок минут',41:'сорок одна минута',42:'сорок две минуты',
        43:'сорок три минуты',44:'сорок четыре минуты'}

hour_с = {1:'первого', 2:'второго', 3:'третьего',4:'четвертого',5:'пятого',6:'шестого',
        7:'седьмого',8:'восьмого',9:'девятого',10:'десятого',11:'одиннадцатого',12:'двенадцатого'}

min_c = {1:'одной минуты', 2:'двух минут', 3:'трех минут',4:'четырех минут',5:'пяти минут',
        6:'шести минут',7:'семи минут',8:'восьми минут',9:'девяти минут',10:'десяти минут',
        11:'одиннадцати минут',12:'двенадцати минут',13:'тринадцати минут',
        14:'четырнадцати минут',15:'пятнадцати минут'}

choice = int(input('Выберете два варианта вывода времени: \
1 - текущее время, 2 - время введенное с консоли:\n'))
if choice ==2:
    time = input('Введите время в формате hh.mm:\n')
    time = time.replace(' ', '')
    
    if len(time) != 5 or time[2] != '.':
        print('вы ввели неверный формат')
        exit()

    time_s = time.split(".")
    c_h = time_s[0]
    c_m = time_s[1]

    if not c_h.isnumeric() or not c_m.isnumeric():
        print('вы ввели неверный формат')
        exit()

    c_h, c_m = int(c_h), int(c_m)

    if c_h > 24 or c_m > 60:
        print('вы ввели неверный формат')
        exit()

else:
    current_time = datetime.datetime.now()
    c_h = current_time.hour
    c_m = current_time.minute

if c_h > 12:
    c_h %= 12

if c_m == 0:
    print(f"{hour[c_h]} ровно")

elif c_m == 30:
    c_h += 1
    print(f"половина {hour_с[c_h]}")

elif (c_m != 0 and c_m < 30) or (c_m > 30 and c_m < 45):
    c_h += 1
    if c_h > 12:
        c_h %= 12
    print(f"{min[c_m]} {hour_с[c_h]}")

elif c_m >= 45:
    c_m = 60 - c_m
    c_h += 1
    print(f"без {min_c[c_m]} {hour_с[c_h]}")
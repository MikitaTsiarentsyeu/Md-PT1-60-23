import datetime
time = input("Для получения текстового вывода времени введите время в формате hh:mm; для получения текущего времени нажмите клавишу enter\n")

if len(time) == 0:
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
elif len(time) == 5 and time[2] == ':':
    h_m = time.split(':')
    h = h_m[0]
    m = h_m[1]
    if not h.isnumeric() or not m.isnumeric():
        print("Введите корректные данные")
        exit()
else:
    print("Введите корректные данные")
    exit()

h, m = int(h), int(m)

d = {1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь',8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать',
 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шеснадцать', 17:'семнадцать', 18:'восемнадцать',
  19:'девятнадцать', 20:'двадцать', 21:'двадцать одна', 22:'двадцать две', 23:'двадцать три', 24:'двадцать четыре', 25:'двадцать пять',
    26:'двадцать шесть', 27:'двадцать семь', 28:'двадцать восемь', 29:'двадцать девять', 31:'дридцать одна', 32:'дридцать две',
     33:'тридцать три', 34:'тридцать четыре', 35:'тридцать пять', 36:'тридцать шесть', 37:'тридцать семь', 38:'тридцать восемь',
      39:'тридцать девять', 40:'сорок', 41:'сорок одна', 42:'сорок две', 43:'сорок три', 44:'сорок четыре', 45:'пятнадцати',
       46:'четырнадцати', 47:'тринадцати', 48:'двенадцати', 49:'одиннадцати', 50:'десяти', 51:'девяти', 52:'восьми', 53:'семи', 54:'шести',
        55:'пяти', 56:'четырех', 57:'трех', 58:'двух', 59:'одной'}
d_h = {1:'второго', 2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 7:'восьмого', 8:'девятого',
9:'десятого', 10:'одиннадцатого', 11:'двенадцатого', 12:'первого', 13:'второго', 14:'третьего', 15:'четвертого',
 16:'пятого', 17:'шестого', 18:'седьмого', 19:'восьмого', 20:'девятого', 21:'десятого', 22:'одиннадцатого',
  23:'двенадцатого', 00:'первого'}
d_e = {00:'двенадцать', 1:'один', 2:'два', 3:'три', 4:'четыре', 13:'один', 14:'два', 15:'три', 16:'четыре', 17:'пять', 18:'шесть',
 19:'семь', 20:'восемь', 21:'девять', 22:'десять', 23:'одиннадцать', 24:'двенадцать'}

if m == 0 and h == 1:
    print(f"{d_e[h]} час ровно")
elif m == 0 and h == 13:
    print(f"{d_e[h]} час ровно")
elif m == 0 and h == 0:
    print(f"{d_e[h]} часов ровно")
elif m == 0 and 5 <= h <= 12:
    print(f"{d[h]} часов ровно")
elif m == 0 and 17 <= h <= 23:
    print(f"{d_e[h]} часов ровно")
elif m == 0 and 2 <= h <= 4:
    print(f"{d_e[h]} часа ровно")
elif m == 0 and 14 <= h <= 16:
    print(f"{d_e[h]} часа ровно")
elif m == 30:
    print(f"половина {d_h[h]}")
elif m == 1 or m == 21 or m == 31 or m == 41:
    print(f"{d[m]} минута {d_h[h]}")
elif 2 <= m <= 4 or 22 <= m <= 24 or 32 <= m <=34 or 42 <= m <= 44:
    print(f"{d[m]} минуты {d_h[h]}")
elif 5 <= m <= 20 or 25 <= m <= 29 or 35 <= m <= 40:
    print(f"{d[m]} минут {d_h[h]}")
elif m == 59 and h == 0:
    print(f"без {d[m]} минуты час")
elif m == 59 and h == 12:
    print(f"без {d[m]} минуты час")
elif m >= 45 and h == 0 or h == 12:
    print(f"без {d[m]} минут час")
elif m >= 45 and 5 <= h <= 11:
    print(f"без {d[m]} минут {d[h + 1]}")
else:
    print(f"без {d[m]} минут {d_e[h + 1]}")







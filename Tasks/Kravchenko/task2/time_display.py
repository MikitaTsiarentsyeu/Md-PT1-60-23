import datetime
user_choice = input('''Please choose time input method. 
Press 1, if you want to enter any time you want manually. 
Press 2 in order to display current time automatically. \n''')
while user_choice not in ["1", "2"]:
    print("Your input was incorrect.")
    user_choice = input('''Please choose time input method. 
        Press 1, if you want to enter any time you want. 
        Press 2 in order to display current time. \n''')
if user_choice == "1":
    manual_time = input('Enter time in hh:mm format.\n')
    manual_time = manual_time.replace(' ', '')
    while len(manual_time) != 5 or manual_time[2] != ':':
        print("Your input was in incorrect format.")
        manual_time = input('Enter time in hh:mm format.\n')
    h_m = manual_time.split(':')
    h = h_m[0]
    m = h_m[1]
    t = f'{h}:{m}'
    if not h.isnumeric() or not m.isnumeric():
        print("Your input was in incorrect format")
        exit()
    h, m = int(h), int(m)
    if (h > 23 or h < 0) or (m > 59 or m < 0):
        print("Your input was in incorrect format")
        exit()
elif user_choice == "2":
    current_time  = datetime.datetime.now()
    h = current_time.hour
    m = current_time.minute
    t = f'{h}:{m}' if m >= 10 else f'{h}:0{m}'
if h > 12:
    h = h - 12
m_1 = m//10
m_2 = m%10
dict = {0:['ноль'], 1:['один', 'одной', 'первого'], 2:['два', 'двух', 'второго'], 3: ['три','трех','третьего'], 
4: ['четыре','четырех','четвертого'], 5: ['пять', 'пяти', 'пятого'], 6: ["шесть","шести",'шестого'], 
7: ["семь", "семи", 'седьмого'], 8: ['восемь', 'восьми', 'восьмого'], 9: ['девять','девяти','девятого'], 
10: ['десять', 'десяти','десятого'], 11: ['одиннадцать','одиннадцати','одиннадцатого'], 
12: ['двенадцать','двенадцати','двенадцатого'], 20: ['двадцать'], 30: ['триддцать'], 40: ['сорок']}
endings_min = {'на':'минута', 'ри':'минуты', 'ре':'минуты', 'ве':'минуты', 'ть':'минут', 'ок':'минут', 'мь':'минут',
'ой':'минуты', 'ух':'минут', 'ех':'минут','ти':'минут', 'ми': 'минут'} 
endings_hours = {'ин':'час', 'ва':'часа', 'ри':'часа','ре':'часа', 'ть':'часов', 'мь':'часов', 'ль':'часов'}
if m_1 == 0 and m_2 == 0:
    b = endings_hours[dict[h][0][-2:]]
    print(f"{t} - {dict[h][0]} {b} ровно")
elif m == 30:  
    print(f"{t} - половина {dict[h+1][2]}") if h < 12 else print(f"{t} - половина {dict[1][2]}")
elif 1 <= m_1 <= 4 and m_2 == 0: 
    b = endings_min[dict[m][0][-2:]]
    print(f"{t} - {dict[m][0]} {b} {dict[h+1][2]}") if h < 12 else print(f"{t} - {dict[m][0]} {b} {dict[1][2]}")
elif m < 10:
    dict[1][0] = "одна"
    dict[2][0] = "две"
    b = endings_min[dict[m_2][0][-2:]]
    print(f"{t} - {dict[m_2][0]} {b} {dict[h+1][2]}") if h < 12 else print(f"{t} - {dict[m_2][0]} {b} {dict[1][2]}")
elif 10 < m < 20:
    dict[2][0] = "две"
    if 4 <= m_2 <= 9:
        dict[m_2][0] = dict[m_2][0][:-1]
    print(f"{t} - {dict[m_2][0]}надцать минут {dict[h+1][2]}") if h < 12 else print(f"{t} - {dict[m_2][0]}надцать минут {dict[1][2]}")
elif 20 < m < 45 and m_2 != 0:
    dict[1][0] = "одна"
    dict[2][0] = "две"
    b = endings_min[dict[m_2][0][-2:]]
    print(f"{t} - {dict[m-m_2][0]} {dict[m_2][0]} {b} {dict[h+1][2]}") if h < 12 else print(f"{t} - {dict[m-m_2][0]} {dict[m_2][0]} {b} {dict[1][2]}")
elif m >= 45:
    m = 60 - m
    dict[13] = ['', 'тринадцати']
    dict[14] = ['', 'четырнадцати']
    dict[15] = ['', 'пятнадцати']
    b = endings_min[dict[m][1][-2:]]
    print(f"{t} - без {dict[m][1]} {b} {dict[h+1][0]}") if 0 < h < 12 else print(f"{t} - без {dict[m][1]} {b} час")



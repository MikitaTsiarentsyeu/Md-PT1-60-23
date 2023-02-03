import datetime

d1 = {1:"один", 2:"два", 3:"три", 4:"четыре", 5:"пять",
6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять",
11:"одинадцать", 12:"двенадцать", 13:"тринадцать",
14:"четырнадцать", 15:"пятнадцать", 16:"шестнадцать",
17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать",
20:"двадцать", 30:"тридцать", 40:"сорок", 50:"пятьдесят",
101:"первого", 102:"второго", 103:"третьего", 104:"четвертого", 
105:"пятого", 106:"шестого", 107:"седьмого", 108:"восьмого", 
109:"девятого", 110:"десятого", 111:"одиннадцатого", 112:"двенадцатого",
201:"одной",202:"двух",203:"трёх",204:"четырёх",205:"пяти",206:"шести",
207:"семи",208:"восьми",209:"девяти", 210:"десяти", 
211:"одиннадцати", 212:"двенадцати", 301:"одна", 302:"две"}

print("Please, print what you need: current_time or your_time?")
user_input = input()
if user_input == "current_time":
    current_time = datetime.datetime.now()
    c_h, c_m = current_time.hour, current_time.minute
    c_h = str(c_h)
    if len(c_h) == 1:
        h = c_h[0]
        c = "0"
    else:
        c = c_h[0]
        h = c_h[1]
    c_h = c + h
    c, h = int(c), int(h)
    c_h = int(c_h)
    c_m = str(c_m)
    c1 = c_m[0]
    m1 = c_m[1]
    c1_m1 = c1 + m1
    c1, m1 = int(c1), int(m1)
    c1_m1 = int(c1_m1)
    if c == 0:
        x = h
    else:
        if c_h < 12:
            x = c_h
        else:
            l = c_h - 12
            x = l
    if c1 == 0:
        x1 = m1
    else:
        x1 = c1_m1
else:
    your_time = input("Enter your time in the format hh.mm:\n")
    if len(your_time) != 5 or your_time[2] != '.':
        print("Your input was in incorrect format")
        exit()
    else:
        i_t = your_time
        c = i_t[0]
        h = i_t[1]
        c_h = c + h
        c, h = int(c),int(h)
        c_h = int(c_h)
        c1 = i_t[3]
        m1 = i_t[4]
        c1_m1 = c1 + m1
        c1, m1 = int(c1), int(m1)
        c1_m1 = int(c1_m1)
        if c == 0:
            x = h
        else:
            if c_h < 12:
                x = c_h
            else:
                l = c_h - 12
                x = l
        if c1 == 0:
            x1 = m1
        else:
            x1 = c1_m1
if x1 == 0:
    if x == 1:
        print(d1[x], "час ровно")
    elif 2 <= x <= 4:
        print(d1[x], "часа ровно")
    else:
        print(d1[x], "часов ровно")
elif 1 <= x1 < 30 or 30 < x1 < 45:
    l = (c1_m1 // 10) * 10
    n = c1_m1 % 10
    x1 = l + n
    x = x + 101
    if x1 == 1:
        print(d1[x1], "минута", d1[x])    
    elif 2 <= x1 <= 4:
        print(d1[x1], "минуты", d1[x])
    elif 5 <= x1 <= 20:
        print(d1[x1], "минут", d1[x])
    else:
        if n == 1:
            n = n + 300
            print(d1[l], d1[n], "минута", d1[x])
        elif n == 2:
            n = n + 300
            print(d1[l], d1[n], "минуты", d1[x])       
        elif 2 < n <= 4:
            print(d1[l], d1[n], "минуты", d1[x])
        else:
            print(d1[l], d1[n], "минут", d1[x])
elif x1 == 30:
    x = x + 1
    print("половина", d1[x])
else:
    x1 = 60 - x1
    if x1 > 1:
        x = x + 1
        x1 = x1 + 200
        print("без", d1[x1], "минут", d1[x])
    else:
        x = x + 1
        x1 = x1 + 200
        print("без", d1[x1], "минуты", d1[x])
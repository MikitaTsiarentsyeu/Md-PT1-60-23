import datetime

minutes, hours = datetime.datetime.now().minute, datetime.datetime.now().hour
m, h = int(minutes), int(hours)

integer_rus = {0 : "Двенадцать часов ночи", 1 : "Час ночи", 2 : "Два часа ночи", 3 : "Три часа ночи", 4 : "Четыре часа утра",
5 : "Пять часов утра", 6 : "Шесть часов утра", 7 : "Семь часов утра", 8 : "Восемь часов утра", 9 : "Девять часов утра",
10 : "Десять часов утра", 11 : "Одинадцать часов утра", 12 : "Двенадцать часов", 13 : "Тринадцать часов",
14 : "Четырнадцать часов", 15 : "Пятнадцать часов", 16 : "Шестнадцать часов", 17 : "Семнадцать часов",
18 : "Восемнадцать часов", 19 : "Девятнадцать часов", 20 : "Двадцать часов", 21 : "Двадцать один час",
22 : "Двадцать два часа", 23 :"Двадцать три часа"}

integer_eng = {0 : "midnight", 1 : "one a.m", 2 : "two a.m", 3 : "three a.m", 4 : "four a.m",
5 : "five a.m", 6 : "six a.m", 7 : "seven a.m", 8 : "eight a.m", 9 : "nine a.m",
10 : "ten a.m", 11 : "eleven a.m", 12 : "midday", 13 : "one p.m", 14 : "two p.m",
15 : "three p.m", 16 : "four p.m", 17 : "five p.m", 18 : "six p.m",
19: "seven p.m", 20 : "eight p.m", 21 : "nine p.m", 22 : "ten p.m",
23 :"eleven p.m"}

minute_rus =  { 1 : "одна минута", 2 : "две минуты", 3 : "три минуты", 4 : "четыре минуты", 5 : "пять минут",
6 : "шесть минут", 7 : "семь минут", 8 : 'восемь минут', 9 : "девять минут", 10 : "десять минут", 11 : "одинадцать минут",
12 : "двенадцать минут", 13 : "тринадцать минут", 14 : "четырнадцать минут", 15 : "пятнадцать минут",
16 : "шестнадцать минут", 17 : "семнадцать минут", 18 : "восемнадцать минут", 19 : "девятнадцать минут",
20 : "двадцать минут", 21 : "двадцать одна минута", 22 : "двадцать две минуты", 23 : "двадцать три минуты",
24 : "двадцать четыре минуты", 25 : "двадцать пять минут", 26 : "двадцать шесть минут", 27 : "двадцать семь минут",
28 : "двадцать восемь минут", 29 : "двадцать девять минут", 30 : "тридцать минут", 31 : "тридцать одна минута",
32 : "тридцать две минуты", 33 : "тридцать три минуты", 34 : "тридцать четыре минуты", 35 : "тридцать пять минут",
36 : "тридцать шесть минут", 37 : "трицать семь минут", 38 : "тридцать восемь минут", 39 : "тридцать девять минут",
40 : "сорок минут", 41 : "сорок одна минута", 42 : "сорок две минуты", 43 : "сорок три минуты",
44 : "сорок четыре минут", 45 : "сорок пять минут", 46 : "сорок шесть минут", 47 : "сорок семь минут",
48 : "сорок восемь минут", 49 : "сорок девять минут", 50 : "пятьдесят минут", 51 : "пятьдесят одна минута",
52 : "пятьдесят две минуты", 53 : "пятьдесят три минуты", 54:"пятьдесят четыри минуты",
55 : "пятьдесят пять минут", 56 : "пятьдесят шесть минут", 57 : "пятьдесят семь минут",
58 : "пятьдесят восемь минут", 59 : "пятьдесят девять минут"}


minute_eng = { 1 : "It's one past", 2 : "It's two past", 3 : "It's three past", 4 : "It's four past",
5 : "It's five past", 6 : "It's six past", 7 : "It's seven past", 8 : "It's eight past", 9 : "It's nine past",
10 : "It's ten past", 11 : "It's eleven past", 12 : "It's twelve past", 13 : "It's thirteen past",
14 : "It's fourteen past", 15 : "It's quarter past", 16 : "It's sixteen past", 17 : "It's seventeen past",
18 : "It's eighteen past", 19 : "It's nineteen past", 20 : "It's twenty past", 21 : "It's twenty one past",
22 : "It's twenty two past", 23 : "It's twenty three past", 24 : "It's twenty four past", 25 : "It's twenty five past",
26 : "It's twenty six past", 27 : "It's twenty seven past",
28 : "It's twenty eight past", 29 : "It's twenty nine past", 30 : "It's half past", 31 : "It's thirty one past",
32 : "It's thirty two past", 33 : "It's thirty three past", 34 : "It's thirty four past", 35 : "It's thirty five past",
36 : "It's thirty six past", 37 : "It's thirty seven past", 38 : "It's thirty eight past", 39 : "It's thirty nine past",
40 : "It's twenty to", 41 : "It's nineteen to", 42 : "It's eighteen to", 43 : "It's seventeen to",
44 : "It's sixteen to", 45 : "Quarter to", 46 : "It's fourteen to", 47 : "It's thirteen to",
48 : "It's twelve to", 49 : "It's eleven to", 50 : "It's ten to", 51 : "It's nine to",
52 : "It's eight to", 53 : "It's seven to", 54:"It's six to",
55 : "It's five to", 56 : "It's four to", 57 : "It's three to",
58 : "It's two to", 59 : "It's one to"}

half_rus = {0 : 'Половина первого ночи', 1 : 'Половина второго ночи', 2 : 'Половина третьего ночи',
3 : 'Половина четвертого ночи', 4 : 'Половина пятого утра', 5 : 'Половина шестого утра', 6 :  'Половина седьмого утра',
7 :  'Половина восьмого утра', 8 : 'Половина девятого утра', 9: 'Половина десятого', 10 :'Половина одиннадцатого',
11 : 'Половина двенадцатого', 12 : 'Половина первого', 13 : 'Половина второго', 14 : 'Половина третьего',
15 : 'Половина четвёртого',16 : 'Половина пятого', 17 : 'Половина шестого', 18 : 'Половина седьмого',
19 : 'Половина восьмого', 20 : 'Половина девятого', 21 : 'Половина десятого вечера',
22 : "Половина одиннадцатого вечера", 23 : "Половина двенадцого ночи"}

half_eng = {0 : 'Half past one a.m', 1: 'Half past two a.m', 2: 'Half past three a.m', 3: 'Half past four a.m',
4: 'Half past five a.m', 5: 'Half past six a.m', 6: 'Half past seven a.m', 7: 'Half past eight a.m',
8: 'Half past nine a.m', 9: 'Half past ten a.m', 10: 'Half past eleven a.m', 11: 'Half past twelve a.m',
12 : 'Half past one p.m', 13: 'Half past two p.m', 14: 'Half past three p.m', 15: 'Half past four p.m',
16: 'Half past five p.m', 17: 'Half past six p.m', 18: 'Half past seven p.m', 19: 'Half past eight p.m',
20: 'Half past nine p.m', 21: 'Half past ten p.m', 22: 'Half past eleven p.m', 23: 'Half past twelve p.m'}

without_rus = {0 : "Без шести минут час ночи", 1 : "Без шести минут два часа ночи",
2 : "Без шести минут три часа ночи", 3 : "Без шести минут четыре часа ночи", 4 : "Без шести минут пять часов утра",
5 : "Без шести минут шесть часов утра", 6 : "Без шести минут семь часов утра", 7 : "Без шести минут восемь часов утра",
8 : "Без шести минут девять часов утра", 9 : "Без шести минут десять часов утра",
10 : "Без шести минут одиннадцать часов утра", 11 : "Без шести минут полдень", 12 : "Без шести минут час дня",
13 : "Без шести минут два часа дня", 14 : "Без шести минут три часа дня", 15 : "Без шести минут четыре часа дня",
16 : "Без шести минут пять часов дня", 17 : "Без шести минут шесть часов вечера", 18 :"Без шести минут семь часов вечера",
19 : "Без шести минут восемь часов вечера", 20 : "Без шести минут девять часов вечера",
21 : "Без шести минут десять часов вечера", 22 : "Без шести минут одиннадцать часов вечера",
23 : "Без шести минут двенадцать часов ночи"}

without_eng = {0 : "Six minutes before one a.m", 1 : "Six minutes before two a.m",
2 : "Six minutes before three a.m", 3 : "Six minutes before four a.m", 4 : "Six minutes before five a.m",
5 : "Six minutes before six a.m", 6 : "Six minutes before seven a.m", 7 : "Six minutes before eight a.m",
8 : "Six minutes before nine a.m", 9 : "Six minutes before ten a.m",
10 : "Six minutes before eleven a.m", 11 : "Six minutes before midday", 12 : "Six minutes before one p.m",
13 : "Six minutes before two p.m", 14 : "Six minutes before three p.m", 15 : "Six minutes before four p.m",
16 : "Six minutes before five p.m", 17 : "Six minutes before six p.m", 18 :"Six minutes before seven p.m",
19 : "Six minutes before eight p.m", 20 : "Six minutes before nine p.m",
21 : "Six minutes before ten p.m", 22 : "Six minutes before eleven p.m",
23 : "Six minutes before midnight"}

name = input('Enter your name:\n')
print(f"Hello, {name}. Its a simple programm to work with time(I know what You want to ask, but unfortunately, no,\n"
      f"it cannot change the time). This programm can indicate You what time right now or show the time you've\n" 
      f"entered with details(description).")
choice = int(input('Please, press "1" to show the time, or "2" to enter your time:\n'))
if choice == 1:

      if h < 10:

            print(f' 0{h}:{m}')
            if m == 0:
                  print(integer_rus.get(h), integer_eng.get(h))
            elif m == 30:
                  print(half_rus(h), half_eng(h))
            elif m == 54:
                  print(without_rus(h), without_eng(h))
            else:
                  print(f' In 24hh format-{integer_rus.get(h)} и {minute_rus.get(m)}\n',
                        f'In 12hh format-{minute_eng.get(m)} and {integer_eng.get(h)}')
      elif m < 10:
            print(f' {h}:0{m}')
            if m == 0:
                  print(integer_rus.get(h), (integer_eng.get(h)))
            elif m == 30:
                  print(half_rus(h), half_eng(h))
            elif m == 54:
                  print(without_rus(h), without_eng(h))
            else:
                  print(f' In 24hh format-{integer_rus.get(h)} и {minute_rus.get(m)}\n',
                        f'In 12hh format-{minute_eng.get(m)} {integer_eng.get(h)}')
      else:
            print(f' {h}:{m}')
            if m == 0:
                  print(integer_rus.get(h), integer_eng.get(h))
            elif m == 30:
                  print(half_rus(h), integer_eng(h))
            elif m == 54:
                  print(without_rus(h), without_eng(h))
            else:
                  print(f' In 24hh format-{integer_rus.get(h)} и {minute_rus.get(m)}\n',
                        f'In 12hh format-{minute_eng.get(m)} {integer_eng.get(h + 1)}')

      if h < 12:
            print(f" It's {h}:{m} o'clock")
            if m == 0:
                  print(integer_rus.get(h), integer_eng.get(h))
            elif m == 30:
                  print(half_rus(h), half_eng(h))
            elif m == 54:
                  print(without_rus(m), without_eng(m))
            else:
                  print(f' In 24hh format-{integer_rus.get(h)} и {minute_rus.get(m)}\n',
                        f'In 12hh format-{minute_eng.get(m)} {integer_eng.get(h)}')


elif choice == 2:
      user_time_hh, user_time_mm = int(input('Enter an hours:\n'), int(input('Enter a minutes:\n')))
      if user_time_mm < 10:
            print(f' {user_time_hh}:0{user_time_mm}')
            if user_time_mm == 0:
                  print(f' {integer_rus.get(user_time_hh)}\n',f'{integer_eng.get(user_time_hh)}')
            elif user_time_mm == 30:
                  print(f' {half_rus.get(user_time_hh)}\n',f'{half_eng.get(user_time_hh)}')
            elif user_time_mm == 54:
                  print(without_rus.get(user_time_hh), without_eng.get(user_time_hh))
            else:
                  print(f'{integer_rus.get(user_time_hh)} и {minute_rus.get(user_time_mm)}\n',
                        f'{minute_eng.get(user_time_mm)} {integer_eng.get(user_time_hh)}')
      else:
            print(f' {user_time_hh}:{user_time_mm}')
            if user_time_mm == 0:
                  print(f' {integer_rus.get(user_time_hh)}\n',f'{integer_eng.get(user_time_hh)}')
            elif user_time_mm == 30:
                  print(f' {half_rus.get(user_time_hh)}\n',f'{half_eng.get(user_time_hh)}')
            elif user_time_mm == 54:
                  print(f' {without_rus.get(user_time_hh)}\n',f'{without_eng.get(user_time_hh)}')
            else:
                  print(f' {integer_rus.get(user_time_hh)} и {minute_rus.get(user_time_mm)}\n',
                        f'{minute_eng.get(user_time_mm)} {integer_eng.get(user_time_hh)}')


else:
      print(f"\033[31mYou've entered incorrect information, try again later!")
input()
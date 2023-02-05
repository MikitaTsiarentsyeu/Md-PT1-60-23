import datetime

minutes, hours = datetime.datetime.now().minute, datetime.datetime.now().hour
m, h = int(minutes), int(hours)

dictionary = {
      0: ["двенадцать", "", "", "",],
      1: ['одна', 'одной', "час", "первого"],
      2: ["две", "двух", "два", "второго"],
      3: ["три", "трех", "", "третьего"],
      4: ["четыри", "четырех", "", "четвертого"],
      5: ["пять", "пяти", "", "пятого"],
      6: ["шесть", "шести", "", "шестого"],
      7: ["семь", "семи", "", "седьмого"],
      8: ["восемь", "восьми", "", "восьмого"],
      9: ["девять", "девяти", "", "девятого"],
      10: ["десять", "десяти", "", "десятого"],
      11: ["одинадцать", "одинадцати", "", "одинадцатого"],
      12: ["двенадцать", "двенадцати", "", "двенадцатого"],
      13: ["тринадцать", "тринадцати", "час", "первого"],
      14: ["четырнадцать", "четырнадцати", "два", "второго"],
      15: ["пятнадцать", "пятнадцати", "три", "третьего"],
      16: ["шестнадцать", "шестнадцати", "четыри", "четвертого"],
      17: ["семнадцать", "семнадцати", "пять", "пятого"],
      18: ["восемнадцать", "восемнадцати", "шесть", "шестого"],
      19: ["девятнадцать", "девятнадцати", "семь", "седьмого"],
      20: ["двадцать", "двадцати", "восемь", "восьмого"],
      21: ["двадцать один", "", "девять", "девятого"],
      22: ["двадцать два", "", "десять", "десятого"],
      23: ["двадцать три", "", "одинадцать", "одинадцатого"],
      24: ["", "", "", "двенадцатого"],
      30: ["тридцать", "половина", "", ""],}

name = input('Введите свое имя:\n')
print(f'Доброго времени суток, {name}. Если хотите узнать точное время c расшифровкой текстом, нажмите "1",\n'
      f'Если хотите указать свое время с расшифровкой текстом, нажмите "2".')
choice = int(input("Введите ответ:\n"))

if choice == 1 and h < 10 and m < 10:
      print(f'0{h}:0{m}')
      if m == 0:
            print(f'{dictionary.get(h)[0]} часов ровно')
      elif m < 30:
            print(f'{dictionary.get(m)[0]} минут {dictionary.get(h + 1)[3]}')
      elif m == 30:
            print(f'{dictionary.get(m)[1]} {dictionary.get(h + 1)[3]}')
      elif m > 30 and m < 59:
            print(f'Без {dictionary.get(60 - m)[1]} минут {dictionary.get(h + 1)[2]}')

elif choice == 1 and h >= 10 and m >= 10:
      print(f'{h}:{m}')
      if m == 0:
            print(f'{dictionary.get(h)[0]} часов ровно')
      elif m < 30:
            print(f'{dictionary.get(m)[0]} минут {dictionary.get(h + 1)[3]}')
      elif m == 30:
            print(f'{dictionary.get(m)[1]} {dictionary.get(h + 1)[3]}')
      elif m > 30 and m < 59:
            print(f'Без {dictionary.get(60 - m)[1]} минут {dictionary.get(h + 1)[2]}')


elif choice == 2:
      user_hh = int(input('Введите кол-во часов:\n'))
      user_mm = int(input('Введите кол-во минут:\n'))
      if user_hh < 10 and user_mm < 10:
            print(f'0{user_hh}:0{user_mm}')
            if user_mm == 0:
                  print(f'{dictionary.get(user_hh)[0]} часов ровно')
            elif user_mm < 30:
                  print(f'{dictionary.get(user_mm)[0]} минут {dictionary.get(user_hh + 1)[3]}')
            elif user_mm == 30:
                  print(f'{dictionary.get(user_mm)[1]} {dictionary.get(user_hh + 1)[3]}')
            elif user_mm > 30 and user_mm < 59:
                  print(f'Без {dictionary.get(60 - user_mm)[1]} минут {dictionary.get(user_hh + 1)[2]}')

      elif user_hh >= 10 and user_mm >= 10:
            print(f'{user_hh}:{user_mm}')
            if user_mm == 0:
                  print(f'{dictionary.get(user_hh)[0]} часов ровно')
            elif user_mm < 30:
                  print(f'{dictionary.get(user_mm)[0]} минут {dictionary.get(user_hh + 1)[3]}')
            elif user_mm == 30:
                  print(f'{dictionary.get(user_mm)[1]} {dictionary.get(user_hh + 1)[3]}')
            elif user_mm > 30 and user_mm < 59:
                  print(f'Без {dictionary.get(60 - user_mm)[1]} минут {dictionary.get(user_hh + 1)[2]}')

else:
      print(f"\033[31mВы ввели другое значение, повторите попытку позже!")
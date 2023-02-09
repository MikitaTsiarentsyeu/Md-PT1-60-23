import datetime

user_input = input(
    'Hi! Do you want to know the current time (press Enter) or enter your own (enter your time in HH:mm)?\n')
time = str(datetime.datetime.now().time())[0:5] if not user_input else user_input
time = '0' + time if time[1] == ':' else time
time = str((int(time[0:2]) - 12)) + ':' + time[3:5] if 13 <= int(time[0:2]) <= 23 else time
time = '0' + time if time[1] == ':' else time

word_base = {'0_1': 'ноль',
             '1_1': 'один', '1_2': 'первого', '1_3': 'одной', '1_4': 'одна',
             '2_1': 'два', '2_2': 'второго', '2_3': 'двух', '2_4': 'две',
             '3_1': 'три', '3_2': 'третьего', '3_3': 'трёх', '3_4': 'тридцать',
             '4_1': 'четыре', '4_2': 'четвертого', '4_3': 'четырёх', '4_4': 'сорок',
             '5_1': 'пять', '5_2': 'пятого',
             '6_1': 'шесть', '6_2': 'шестого',
             '7_1': 'семь', '7_2': 'седьмого',
             '8_1': 'восемь', '8_2': 'восьмого',
             '9_1': 'девять', '9_2': 'девятого',
             '10_1': 'десять', '10_2': 'десятого',
             '11_1': 'одинадцать', '11_2': 'одинадцатого',
             '12_1': 'двенадцать', '12_2': 'двенадцатого',
             '13_1': 'тринадцать', '13_2': 'первого',
             '14_1': 'четырнадцать', '15_1': 'пятнадцать', '16_1': 'шестнадцать', '17_1': 'семнадцать',
             '18_1': 'восемнадцать', '19_1': 'девятнадцать', '20_1': 'двадцать'}

if time[3:5] == '00':
    print(word_base.get(f'{int(time[0:2])}_1') + ' часов ровно')
elif int(time[3:5]) < 30:
    if int(time[3:5]) == 1:
        print(word_base.get('1_4') + ' минута ' + word_base.get(f'{int(time[0:2]) + 1}_2'))
    elif int(time[3:5]) == 2:
        print(word_base.get('2_4') + ' минуты ' + word_base.get(f'{int(time[0:2]) + 1}_2'))
    elif 3 <= int(time[3:5]) <= 4:
        print(word_base.get(f'{int(time[3:5])}_1') + ' минуты ' + word_base.get(f'{int(time[0:2]) + 1}_2'))
    elif 5 <= int(time[3:5]) <= 20:
        print(word_base.get(f'{int(time[3:5])}_1') + ' минут ' + word_base.get(f'{int(time[0:2]) + 1}_2'))
    else:
        print(word_base.get('20_1') + ' ' + word_base.get(f'{int(time[4])}_1') + ' минут ' +
              word_base.get(f'{int(time[0:2]) + 1}_2'))
elif int(time[3:5]) == 30:
    print('половина ' + word_base.get(f'{int(time[0:2]) + 1}_2'))
elif 30 < int(time[3:5]) < 45:
    print(word_base.get(f'{int(time[3])}_4') + ' ' + word_base.get(f'{int(time[4])}_1') + ' минут ' +
          word_base.get(f'{int(time[0:2]) + 1}_2'))
else:
    if 45 <= int(time[3:5]) <= 55:
        print('без ' + word_base.get(f'{60 - int(time[3:5])}_1')[:-1] + 'и' + ' минут ' + word_base.get(
            f'{int(time[0:2]) + 1}_1'))
    else:
        print('без ' + word_base.get(f'{60 - int(time[3:5])}_3') + ' минут ' + word_base.get(
            f'{int(time[0:2]) + 1}_1'))


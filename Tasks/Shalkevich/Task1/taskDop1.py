from  collections import Counter
import pandas as pd
# Что за не уважения к квадратам?) За кубическое уровнения 100 баллов, а за квадратное 0((
print("Привет! ЧЕЛОВЕК. Я КОМПЬЮТЕР И Я УМНЕЕ ТЕБЯ! У меня памяти 16 мегабайт!!")
# Интересно, сколько людей помнят этот мем?)
print()
print("Я умею читать, писать, и... много чего умею. Вот ты сейчас напиши мне и я посчитаю всё!")
while True:
    ansver = str(input("Введи, что угодно.Я могу всё! "))
    print("У меня есть 2 решения, какой ты хочещь увидеть? 1, 2?")
    c = Counter(ansver)
    try:
        W = input()
        W = int(W)
        if W == 1:
            Tex1 = len(ansver)
            Tex = {'Пробел': 0, 'Букв': 0, 'Цифр': 0}
            for i in ansver:
                if i.isalpha():
                    Tex['Букв'] += 1
                elif i.isdigit():
                    Tex['Цифр'] += 1
                else:
                    Tex['Пробел'] += 1
            print("Так.. Сейчас посчитаю... так.. 1... Длина твоего текста ", Tex1,
            " Символов! Из которых ", Tex, "из которых")
            print()
            print(dict(Counter(c)))
        elif W ==2:
            print(list(ansver))
            print (pd.Series(list(ansver)).value_counts())
        else:
            print("Глуппый человек, я прошу выбрать 1 или 2 - это такие цифры, если не знаешь")
            continue
    except ValueError:
        print("Глуппый человек, я прошу выбрать 1 или 2 - это такие цифры, если не знаешь")
        continue
    print("Ты признаёшь мою победу, или повторить?) (1 - повторить), (2 - Признать, победу)")
    a = input()
    try:
        a = int(a)
        if a == 1:
            print("Не можешь признать мою победу?). Хорошо")
            continue
        elif a == 2:
            print("ДА! Я вновь победил! Но... Ты тоже ничего, давай ещё как-нибудь поиграем")
            raise SystemExit
        else:
            print("Я знал, что я лучший! Прощай!")
            raise SystemExit
    except ValueError:
        print("Я знал, что я лучший! Прощай!")
        raise SystemExit
import math
print("Добро пожаловать в наш банк 'ООО ДОМ ПОД ЗАЛОГ! Чего вы желаете? Взять кредит или сделать депозит?")
print()
while True:
    print("Если хотите оформить кредит, нажмите 2, если желаете открыть депозит нажмите 1")
    ansver = input()
    try:
        ansver = int(ansver)
        if ansver == 1:
            print("Укажите пожалуйста, какую сумму вы хотете вложить?")
            money = input()
            try:
                money = float(money)
                print("Вы желаете вложить в наш чудесный банк сумму,", (round(money, 2)),
                "рублей на сколько лет вы планируйте вложить ваши средства?")
                data = input()
                try:
                    data = int(data)
                    print("Хорошо.. вы предполагаете, что сможете вернуть  деньги из нашего банка в течение", data,
                    "лет.. Наивный человек. И какой же процент устроит вашу скромную персону?)")
                    Percent = input()
                    try:
                        Percent = float(Percent)
                        if Percent > 30:
                            print("Какой хитрый человек сегодня попался.. решил разорить наш прекрасный банк?? "
                            "Ты хочешь,", (round(Percent, 2)),
                            "процентную ставку по вашему депозиту, но сегодня твой день и я одобряю это")
                            print()
                            it = (money * Percent * data) / 365
                            print("Итак.... Персональный процент, два в уме.. умножить на 6... и прибавить это"
                            "... Итого.. вы получите от нашего выгодного сотрудничества,"
                            , (round(it, 2)), " рублей. Спасибо за депозит! Вы не просили? "
                            "А мы и не спрашивали! Мы рады сообщить, что застраховали ваше здоровье "
                            "в компание партнёре ОАО 'СПАСИиСОХРАНИ' по этому не болейте, досвидение")
                            break
                        else:
                            print("А вот такое мне нравится, может сразу несколько кредитов оформим?) Вы желаете,",
                            (round(Percent, 2)),
                            "процентную ставку по вашему Вкладу. Принято, теперь начнём подсчёты!")
                            print()
                            it = (money * Percent * data) / 365
                            print("Итак.... Персональный процент, два в уме.. умножить на 6... и прибавить это"
                            "... Итого.. вы получите от нашего выгодного сотрудничества,"
                            , (round(it, 2)), " рублей. Спасибо за депозит! Вы не просили? "
                            "А мы и не спрашивали! Мы рады сообщить, что застраховали ваше здоровье "
                            "в компании партнёре ОАО 'СПАСИиСОХРАНИ' по этому не болейте, Хорошего дня!")
                            break
                    except ValueError:
                        print("Ты можешь писать цифры?? Ты вновь испортил документы!! Теперь придётся вновь"
                        "начинать с начала, так... какую ты там сумму хотел взять от нашего прекрасного банка?")
                    continue
                except ValueError:
                    print("Это что за дата такая??? Я тут документы заполняю, если вы не заметили, напишите Число!"
                    "Давайте теперь повторим с самого начала укажите сумму.")
                continue
            except ValueError:
                print("Это что за сумма такая??? Напишите сумму в рублях!")
                continue

        elif ansver == 2:
            print("Прекрасный выбор, уважаемый, в нашем банке лучшие условия для оформления кредита, "
            "всего-то 80 процентов в месяцОднако компания-партнёр специализирующие на математических науках "
            "'ГУМАНИТАРИИиКОМПАНИЯ', предлагает более выгодные условия для тех, кто решит их уравнения, для решения "
            "его вы можете сами выбрать цифры.")
            print()
        while True:
            print("Вот ваше уравнение ax^2 + bx + c = 0")
            a = input()
            b = input()
            c = input()
            try:
                a,b,c = float(a),float(b),float(c)
                print("Вы с гордостью и медалью со школьной олимпиады по математике 'Зубрёнок'....за 3-й класс.."
                      "взялись за решения уравнения")
                discr = b ** 2 -4 * a * c
                if discr > 0:
                    X1 =(-b + math.sqrt(discr))/ (2 * a)
                    X2 = (-b - math.sqrt(discr)) / (2 * a)
                    print("x1 = ", round(X1,2), "x2 = ", round(X2,2))
                    break
                elif discr == 0:
                    X = (-b) / (2 * a)
                    print("X = ", round(X,2) )
                    break
                else:
                    print("корней нет")
                    break
            except ValueError:
                print("Ты наверное не правильно понял , когда тебя просили вести цифры?")
    except ValueError:
        print("Вы ошиблись банком? Нет такой функции, попробуйте ещё")
        continue
print()
print("Впечатляет, вы сделали это и получаете от нашего банка 10000 долларов на 20 лет, без процентов")





import math
from cmath import *
import requests
import webbrowser

#Первое и основное задание с расчетом вклада под проценты

bank = "КРЕДИТНОЕ ОЧКО"
print(f'                                                                      Случай в банке\n'
      f'                                                                            ....\n'
      f'                                                                            ....\n'
      f'                                                                            ....\n'
      f'                                                                            ....')

print(f'Здраствуйте, рады приветсвовать Вас в нашем банке {bank}.\n'
        f'Меня зовут {bank}v2.0, специально разработанная компьютерная система для работы с клиентами.\n'
        f'Я буду Вашим путеводителем в мире нашего банка! Как я могу к Вам обращаться?\n')
name = input('Введите свое имя:\n')
print(f'{name}, перед Вами расположен дисплей, где Вы можете выбрать услугу, прошу Вас. Выберите нужный Вам вариант.\n'
        f'Информация о депозите, нажмите "1"\n'
        f'Информация о кредитование, нажмите "2"\n'
        f'Актуальные курсы валют, нажмите "3" ')

choice = int(input())
if choice == 1:
    print('Мы очень ценим в нашем банке вкладчиков и предлагаем хорошую % ставку в зависимости от суммы вклада.\n'
          'Какую сумму Вы рассматриваете в качестве вклада ? Введите данные:\n')
    sum = float(input())

    if sum >= 1000:
        print(f'С Вашей кругленькой суммой в {sum} рублей, наш банк предлагает Вам % ставку в размере 8% годовых. Круто, да?')
        percent = .08

        print(f'На какое время Вы хотите сделать вклад?(Прошу учесть, что минимальный период вклада - 1 год.')
        duration = int(input())
        n = 365

        print(f'Давайте уточним, Вы хотите сделать вклад на сумму {sum} рублей под 8%, на {duration} год(а)/лет, все правильно?\n'
        'Выберите "+"/"-"')
        answer = input()
        if answer == '+':

            final_sum = sum * ( pow ((1 + percent / n), n * duration))
            print(f'Положив {sum} рублей под 8% годов сроком на {duration}год(а)/лет, по истечении срока мы Вам выплатим {round(final_sum, 2)} рублей.')
            income = sum * (pow((1 + percent / n), n * duration)) - sum
            print(f'Чистый доход будет составлять: {round(income, 2)} рублей.'
                  'Спасибо, что доверяете своему "Кредитному ОЧКУ". Хорошего Вам дня!')

        else:
            print(f'Очень жаль :( Теперь наш банк {bank} не поможет Вам выбраться с Вашего "ОЧКА". Всего хорошего..')

    else:
        print('Прошу прощения, но с такой суммой для вклада Вы зря выбрали эту вкладку')

elif choice == 2:
    print(f'Для получения кредита возьмите номерок и ожидайте своей очереди! Талончик можно взять в соседнем аппарате!')

else:
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    print('USD:')
    print(round(data['Valute']['USD']['Value'], 2))
    print('EURO:')
    print(round(data['Valute']['EUR']['Value'], 2))

# Пример квадратного уравнения

print(f'Вижу кредит Вы не взяли, значит вы не так глупы, так что в качестве бонуса\n'
'покажу Вам как решать квадратное уравнение! Приступим скорее !!!')
print('\033[31m Введите данные для переменных a, b, c в одну строку через пробел')
a, b, c = map (float, input(f'a = ''b = ''c = ').split())
""""""
a = float(input('a = '))  #Так выглядит красивее, но через map меньше кода ))
b = float(input('b = '))
c = float(input('c = '))
""""""
""""""
d = b ** 2 - 4 * a * c  #Дискриминант

if d < 0:
    print('\033[33m Корней нет:(')
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print('\033[34mx1=', '{:6.2f}'.format(x1))
    print('x2=', '{:6.2f}'.format(x2))

# Пример кубического уравнения по упрощенной формуле имеет только параметры c и d (также известные как p и q)
print('Как Вы поняли, на квадратном уравнении мы не останавливаемся, а развиваемся дальше\n'
      'и теперь нас ждет кубическое уравнение. Ну что, вдох, выдох и мы опять игр... Ой, прошу прощения !\n'
      'Я хотел сказать и поехали смотреть за решением !!!')
print('Введите данные для решения кубического уравнения:')
p = float(input('Значение p = '))
q = float(input('Значение q = '))
def cubic(p,q):
    n = -q/2
    s = (q*q/4+p**3/27)**0.5
    r0 = (n-s)**(1/3)+(n+s)**(1/3)
    r1 = (n+s)**(1/3)+(n+s)**(1/3)
    r2 = (n-s)**(1/3)+(n-s)**(1/3)
    return (r0,r1,r2)

print(cubic(p, q))
print('Данное решение сделал после просмотра видео одного зарубежного математика\n'
      'Ссылка на его видео в YouTube:')
""""" #Здесь я использовал модуль webbrowser, но он дает не кликабельную ссылку, а после завершения программы перекидывает
на указанный мною ютуб канал.... При работе, мой компуктер или хром(я не до конца понял) не вывозят этот переход и пытяясь открыть хром,
закрывают и пайчарм, и недогруженный хром, поэтому я оставлю ссылку закомментированной, чтобы твой компуктер это пережил )
webbrowser.open_new('https://www.youtube.com/watch?v=N-KXStupwsc')
"""""











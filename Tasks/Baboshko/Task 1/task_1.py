from decimal import Decimal
sum_cash = Decimal(input('Какую сумму хотите внести на вклад?: \n'))
time = Decimal(input('На какой срок хотите внести средства (в днях)?:\n'))
interest_rate = Decimal(input('Под какой процент хотите внести средства?:\n'))
income_cash = sum_cash * (((time/365) * (interest_rate/100)) + 1)
rubles = int(income_cash // 1)
#coins = (income_cash % 1) // 0.01 Decimal конфликтует с Float
print('По окончании периода действия вклада банк вам выдаст', income_cash.quantize(Decimal("1.00")), 'руб.')

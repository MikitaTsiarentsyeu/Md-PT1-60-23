ini_deposit = int(input('Введите сумму в рублях: \n'))
n_days = int(input('Введите количество дней вклада: \n'))
int_rate = float(input('Введите процентную ставку: \n'))
int_income = ini_deposit*(int_rate/100)*(n_days/365)
total_income = ini_deposit + int_income
print('Баланс вашего счета составляет', int(total_income), 'руб.', int((total_income - int(total_income))*100), 'коп.')


import math
ini_deposit = int(input())
n_days = int(input())
int_rate = float(input())
int_income = ini_deposit*(int_rate/100)*(n_days/365)
total_income = ini_deposit + int_income
print('Баланс вашего счета составляет', math.floor(total_income), 'руб.', math.floor((total_income - math.floor(total_income))*100), 'коп.')


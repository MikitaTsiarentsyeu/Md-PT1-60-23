import math

a = int(input("Введите вашу сумму (в рублях) :\n")) 
b = int(input("Введите срок (в годах):\n"))
c = int(input("Введите годовой процент:\n"))

d = int((a * ((1 + (c/12))*(12 * b))) - a)

print('Ваш доход на счету в конце указанного срока составит ' + str(d) + ' рублей')


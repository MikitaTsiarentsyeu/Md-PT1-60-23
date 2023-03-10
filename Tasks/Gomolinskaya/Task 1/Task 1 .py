import math

c = float(input ("Ведите начальную сумму вклада: \n"))
n = int(input ("Введите срок (в годах): \n"))
p = int(input ("Введите годовой процент: \n"))

s=c

for x in range(0,n):

    s = s / 100 * p + s
    print("Количество средств за", n, "лет составит", s,"рублей")
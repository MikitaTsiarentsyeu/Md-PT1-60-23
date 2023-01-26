import math
import cmath
import gmpy2
import re
print("Чтобы решить кубическое уравнение формата ax^3 + bx^2 + cx + d = 0, введите следущие коэффициенты:")
a, b, c, d = float(input("a: ")), float(input("b: ")), float(
    input("c: ")), float(input("d: "))

# Формула Кардано
p = (3*a*c - b*b)/(3*a**2)
q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)
D = (p/3)**3 + (q/2)**2
if -0.000000001 < D < 0.0000000001:  # Убираем погрешность вычисления дискриминанта, чтобы он действительно мог равняться 0
    D = 0
if D < 0:  # если возводить отрицательнок число в степень 1/3, то питон криво считает,
    # а gmpy2.root не работает с комплексными числами, поэтому пришлось писать этот if
    alpha = (-q/2 + cmath.sqrt(D))**(1/3)
    beta = (-q/2 - cmath.sqrt(D))**(1/3)
else:
    alpha = gmpy2.root(-q/2 + math.sqrt(D), 3)
    beta = gmpy2.root(-q/2 - math.sqrt(D), 3)
y1 = alpha + beta
y2 = (-alpha - beta)/2 + (complex(0, 1)*(alpha - beta)*math.sqrt(3))/2
y3 = (-alpha - beta)/2 - (complex(0, 1)*(alpha - beta)*math.sqrt(3))/2
x1, x2, x3 = y1 - b/(3*a), y2 - b/(3*a), y3 - b/(3*a)

# Нашли корни уравнений, дальше приводим к нормальному виду

# сокращаем до 3х знаков после запятой
x1 = complex(round(x1.real, 3), round(x1.imag, 3))
x2 = complex(round(x2.real, 3), round(x2.imag, 3))
x3 = complex(round(x3.real, 3), round(x3.imag, 3))

# приводим к float те корни, у которых мнимая часть равна 0
if x1.imag == 0:
    x1 = float(x1.real)
if x2.imag == 0:
    x2 = float(x2.real)
if x3.imag == 0:
    x3 = float(x3.real)

# убираем 0 у float, если они целые
if type(x1) == float and x1 == int(x1):
    x1 = int(x1)
if type(x2) == float and x2 == int(x2):
    x2 = int(x2)
if type(x3) == float and x3 == int(x3):
    x3 = int(x3)

# переводим все в строки, что бы убрать скобки из вывода
x1, x2, x3 = str(x1), str(x2), str(x3)
x1 = re.sub('\(*\)*', '', x1)
x2 = re.sub('\(*\)*', '', x2)
x3 = re.sub('\(*\)*', '', x3)

print("Корни уравнений равны:\nx1 =", x1, "\nx2 =", x2, "\nx3 =", x3)

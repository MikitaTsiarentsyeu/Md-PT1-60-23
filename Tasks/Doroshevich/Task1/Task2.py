import math
a, b, c, d = float(input("Введите коэффициент a:\n")), float(input("Введите коэффициент b:\n")), float(
    input("Введите коэффициент c:\n")), float(input("Введите коэффициент d:\n"))
print("Ваше уравнение имеет вид: " + str(a) + "x^3 + " +
      str(b) + "x^2 + " + str(c) + "x + " + str(d) + " = 0")
# Формула Кардано
# Примем x = y - b/3a
p = (3*a*c - b*b)/(3*a*a)
q = (2*b*b*b - 9*a*b*c + 27*a*a*d)/(27*a*a*a)
print("Канонический трехчленный вид: у^3 + " +
      str(p) + "y + " + str(q) + " = 0")
print(math.sqrt(-2))
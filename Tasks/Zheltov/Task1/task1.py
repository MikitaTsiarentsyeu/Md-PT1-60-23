import math
a = float(input("Enter the amount in rubles:\n"))
b = float(input("Term in years:\n"))
c = float(input("Annual percentage:\n"))

g = (a*((1+(c/100))**b))


print (round(g, 1))  
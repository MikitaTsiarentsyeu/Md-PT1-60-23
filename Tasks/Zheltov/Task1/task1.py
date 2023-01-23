import math
a = int(input("Enter the amount in rubles:\n"))
b = int(input("Term in years:\n"))
c = int(input("Annual percentage:\n"))

g = (a*((1+(c/100))**b))


print (round(g, 1))  
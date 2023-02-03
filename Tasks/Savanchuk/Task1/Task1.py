import math
a = int(input("Enter deposit amount:\n"))
n = int(input("Enter term in years:\n"))
c =  int(input("Enter interest rate:\n"))

print(f"Profit will be: {float(round(a*(1+(c/100))**n))}")
a = float(input("Enter the a value:\n"))
b = float(input("Enter the b value:\n"))
c = float(input("Enter the c value:\n"))

D = b*b - 4*a*c
print(D)

if D > 0:
    x1, x2 = (-b - D**0.5)/(2*a), (-b + D**0.5)/(2*a)
    print(x1, x2)
elif D == 0:
    x = -b/(2*a)
    print(x)
else:
    print("there are no roots")
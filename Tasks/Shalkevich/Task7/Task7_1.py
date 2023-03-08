def Summa(a, b):
    try:
       c = a / b
    except ZeroDivisionError:
        return print("Cannot divide by zero")
    return print(round(c, 2))

(Summa(int(input()),int(input())))

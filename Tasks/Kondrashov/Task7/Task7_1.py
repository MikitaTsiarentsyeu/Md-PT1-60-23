def division(a, b):
    if a and b != 0:
        return print(a // b)
    else:
        try:
            a / b
        except ZeroDivisionError:
            return print('Cannot divide by zero')

division(a=int(input()), b=int(input()))
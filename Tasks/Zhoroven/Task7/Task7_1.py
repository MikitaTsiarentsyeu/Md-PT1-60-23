def div_int(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return print("Cannot divide by zero")


print(div_int(1, 0))

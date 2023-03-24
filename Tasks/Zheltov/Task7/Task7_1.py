def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("На ноль не делится")
        return False

a = int(input("Первое число\n"))
b = int(input("Второе число\n"))
print(div(a, b))
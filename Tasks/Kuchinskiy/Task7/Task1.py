def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return False

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
print(div(a, b))
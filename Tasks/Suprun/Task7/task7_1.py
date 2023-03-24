x = int(input("Input the divident:\n"))
y = int(input("Input the divisor:\n"))
def division(a, b):
    return a/b
try:
    print(division(x, y))
except ZeroDivisionError:
    print("Cannot divide by zero")
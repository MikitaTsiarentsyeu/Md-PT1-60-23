x = int(input())
y = int(input())
def division(a, b):
    return a / b

try:
    division(x, y)
except ZeroDivisionError:
    print('Нельзя делить на ноль!')


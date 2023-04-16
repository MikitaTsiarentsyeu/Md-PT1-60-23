
num_1 = int(input('Введите делимое: '))
num_2 = int(input('Введите делитель: '))
try:
    result = num_1 / num_2

    print(f"Результат деления равен: {result}")
except (ZeroDivisionError, ValueError):
    print("Не удается разделить на ноль")

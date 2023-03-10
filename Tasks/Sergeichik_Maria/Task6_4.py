def pow(number, power):
    if power != 0:
        return number * pow(number, power - 1)
    else:
        return 1


a = input("Введите число:\n")
b = input("Введите степень:\n")
print("Результат:", pow(int(a), int(b)))
a = int(input("Введите первое число:\n"))
b = int(input("Введите второе число:\n"))

try:
    res = a / b
    print(res)

except:
    if b == 0:
        print("Делитель равен нулю")
    else:
        print("Нот фаунд")
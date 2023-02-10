print("Как же сложно всё, числа сложные, уровнение сложные, даже числа сложные, давай найдём простое число?)")
while True:
    nomber = input("число до которого считать числа")
    try:
        nomber = int(nomber)
        break
    except ValueError:
        print("Это не число!")
b = 0
for i in range(2,nomber // 2 + 1):
    if nomber % i == 0:
     b = b+1
if b <= 0:
    print("УРАААААААААААА Вот она простота")
else:
    print("опять... Сложность бытия")

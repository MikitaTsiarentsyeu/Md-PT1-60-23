print("Я великий, математический генний. Я способен моментально не только считать, но и писать числа. ВАУУУ")
while True:
    nomber1, nomber2 = input("число от которого считать числа"), input("число до которого считать числа")
    try:
        nomber1, nomber2 = int(nomber1), int(nomber2)
        break
    except ValueError:
        print("Это не число!")
print("Отлично, теперь я посчитаю все ЧЁТНЫЕ цифры и выведу сумму")
nombers = 0
summa = 0
for i in range(nomber1, nomber2 + 1):
    if i % 2 == 0:
        nombers =+ i
        summa = summa + i
        print(" Итак... Посчитаем", nombers, summa)

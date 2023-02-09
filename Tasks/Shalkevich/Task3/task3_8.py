print("что-то большее, что-то меньшее, а где золотая середина??? Давай найдём золотую середину твоих чисел")
while True:
    nomber1, nomber2 = input("число от которого считать числа"), input("число до которого считать числа")
    try:
        nomber1, nomber2 = int(nomber1), int(nomber2)
        break
    except ValueError:
        print("Это не число!")
print("Отлично, теперь найдём золотую середину")
count = 0
summa = 0
for i in range(nomber1, nomber2 + 1):
    count =+ i
    summa = summa + i

summa = summa / count
print(" Итак... Посчитаем у вас чисел", count, "Золотая середина ваших чисел", round(summa))

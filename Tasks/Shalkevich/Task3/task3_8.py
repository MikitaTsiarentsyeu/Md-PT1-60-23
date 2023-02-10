print("что-то большее, что-то меньшее, а где золотая середина??? Давай найдём золотую середину твоих чисел")
nombers = []
while True:
    nomber = input("чтобы выйти нажмите 0")
    try:
        nomber = int(nomber)
        if nomber !=0:
            nombers.append(nomber)
            continue
        else:
            break
    except ValueError:
        print("Это не число!")
print("Отлично, теперь найдём золотую середину")
count = 0
summa = 0
for i in nombers:
    count += 1
    summa += i
    summa = summa / count


summa = summa / count
print(" Итак... ваши числа",nombers,"Посчитаем у вас чисел", count, "Золотая середина ваших чисел", round(summa))

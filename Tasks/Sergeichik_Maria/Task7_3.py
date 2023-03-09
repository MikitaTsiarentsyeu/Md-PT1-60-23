def CountSum (listofNumbers):
    res = 0
    try:
        for i in listofNumbers:
            if int(i) % 2 == 0:
                res += int(i)

    except TypeError:
        print("Недопустимый тип ввода")

    except:
        print("Неизвестная ошибка")

    return res        

countString = input("Введите кол-во чисел:\n")
listOfString = list()

for i in range(int(countString)):
    listOfString.append(input("Введите число: \n"))

print("Сумма четных чисел равна: " + str(CountSum(listOfString)))

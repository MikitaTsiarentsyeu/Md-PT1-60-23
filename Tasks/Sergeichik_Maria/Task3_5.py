amountOfString = input("Введите количество вводимых строк: \n")
listOfString = list()

for i in range(int(amountOfString)):
    listOfString.append(input("Введите строку: \n"))

print("результат:")

for i in listOfString:
    if len(i) > 5:
        print(i)
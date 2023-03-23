def sortStrings (strings, count):
    resStrings = list()
    for i in strings:
        if len (i) > count:
            resStrings.append(i)
    return resStrings


countString = input("Введите кол-во строк:\n")
listOfString = list()

for i in range(int(countString)):
    listOfString.append(input("Введите строку: \n"))

countSymbols = input("Введите минимальное кол-во символов  в строке:\n")

resultList = sortStrings(listOfString, int(countSymbols))

for s in resultList:
    print(s)
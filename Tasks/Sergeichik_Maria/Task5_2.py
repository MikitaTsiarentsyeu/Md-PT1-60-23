def reverse (strings):
    newList = list()
    for s in strings:
        left = s
        right = ''

        for i in range(len(left)-1,-1,-1):
            right += left[i]

        newList.append(right)   
    return newList    





countString = input("Введите кол-во строк:\n")
listOfString = list()

for i in range(int(countString)):
    listOfString.append(input("Введите строку: \n"))

reversList = reverse(listOfString)

for s in reversList:
    print(s)
example = input("Введите  предложение: \n")
words = example.split(" ")
myDict = dict()
for i in words:
    if len(myDict) == 0:
        myDict[i] = 1
        continue
    
    isFound = False

    for y in myDict:
        if i == y:
            myDict[y] = myDict[y]+1
            isFound = True
            continue

    if isFound == False:
        myDict[i] = 1

for i in myDict:
    print(i + " " + str(myDict[i]))
smth = input("Введите числа через пробел: \n")
masstr = smth.split(" ")
maxValue = 0
lilMax = 0

for x in masstr:
    curValue = int(x)
    if curValue > maxValue:
        lilMax = maxValue
        maxValue = curValue
    elif curValue > lilMax:
        lilMax = curValue

print(lilMax)

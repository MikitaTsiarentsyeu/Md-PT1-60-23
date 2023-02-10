inputtStr = input("Введите ряд чисел: \n")
numbers = inputtStr.split(" ")
result = 0

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
        
    return d == n

for i in numbers:
    currentValue = int(i)

    if IsPrime(currentValue) & currentValue > result:
        result = currentValue

print(result)




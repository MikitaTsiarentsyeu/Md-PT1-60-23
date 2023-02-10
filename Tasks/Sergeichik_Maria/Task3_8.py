numbers = input("Введите список чисел: \n")
smth = numbers.split(" ")
sumValue = 0

for i in smth:  
    sumValue += int(i)
    
result = sumValue / len(smth)
print(result)

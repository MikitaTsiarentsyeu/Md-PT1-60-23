#x = input ("Введите список чисел\n")
x =("22 33 44 55 7 8")
x = x.split(" ")
for i in range(len(x)):
    x[i] = int(x[i])
x1 = x[0]

for i in range (1, len(x)):
    x1 = x1 +x[i]
x2 = x1/len(x)
print ("Среднее арифметическое:", x2)
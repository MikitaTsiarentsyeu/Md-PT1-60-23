x = input ("Введите строку\n")
x1 = []
x = list (x)
for i in range (len(x)):
    if x[i].isupper():
        x1.append(x[i].lower())
    elif x[i].islower():
        x1.append(x[i].upper())
x1 = " ".join(x1)
print ("Отраженный регистр:", x1)
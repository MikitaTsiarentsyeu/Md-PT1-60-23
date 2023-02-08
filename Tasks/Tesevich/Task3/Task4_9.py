x = input ("Введите строку\n")
x = list (x)
x1 = []
for i in x:
    x1.insert(0,i) 
x1 = " ".join(x1)
print ("Обратная строка:", x1)

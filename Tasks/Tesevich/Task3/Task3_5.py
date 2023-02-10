x = input ("Введите строку\n")
x = x.split(" ")
list5 = []
for i in range (len(x)):
    r = x[i]
    if len(r) >= 5:
        list5.append(r)
print (list5)
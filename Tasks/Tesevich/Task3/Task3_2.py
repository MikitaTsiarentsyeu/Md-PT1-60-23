x = input ("Введите список чисел\n")
x = x.split(" ")
summ = []
for i in x:
        i = int(i)
        if i % 2 == 0:
            summ.append (i)    
summ = sum(summ)
print ("Сумма равна: ", (summ))

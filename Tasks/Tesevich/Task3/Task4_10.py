import math
x1 = input ("Введите строку \n")

x1 = x1.split(" ")
x = []
smp = []
minilist = []
for i in range(len(x1)):
    x1[i] = int(x1[i])
    x.append(x1[i])
i = 0

for i in x:
    mn = 2
    while mn**2 <= i and i != 1 and i != 0:
        if i % mn == 0:
                    break
        else: mn=mn +1
    else:
        smp.append(i)

r=1
i = 0
while len(smp) > 2:
    for i in range(len(smp)):
        if smp[i] < smp[r]:
            r=i
    f = smp.pop(r)
    r=r-1
    minilist.append(f)
    
if smp[0] < smp[1]:
    print ("Наибольшее простое число:", (smp[1]))
else:
    print ("Наибольшее простое число:", (smp[0]))
    



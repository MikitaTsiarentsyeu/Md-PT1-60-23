x1 = input ("Введите строку\n")
x1 = x1.split(" ")
x = []
for i in range(len(x1)):
    x1[i] = int(x1[i])
    x.append(x1[i])
r=0
minilist = []
while len(x) > 2:
    for i in range(len(x)):
        if x[i] < x[r]:
            r=i
    f = x.pop(r)
    r=r-1
    minilist.append(f)
if x[0] > x[1]:
    print ("Второе наибольшее число:", (x[1]))
else:
    print ("Второе наибольшее число:", (x[0]))
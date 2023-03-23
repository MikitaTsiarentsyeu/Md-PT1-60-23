S = input("Input your space-separated numbers:\n").split(",")
p =[]
for i in S:
    if int(i) % 2 == 0 or int(i) % 3 == 0 or int(i) % 5 == 0:
        continue
    else:
        p.append(int(i))
if "2" in S:
    p.append(2)
else:
    pass
if "3" in S:
    p.append(3)
else:
    pass
if "5" in S:
    p.append(5)
else:
    pass
p.sort()
print(p[-1])
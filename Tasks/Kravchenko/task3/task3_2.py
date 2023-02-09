n = input().split()
s = 0
for i in n: 
    i = int(i)
    if i %2 == 0:
        s += i
print(s)

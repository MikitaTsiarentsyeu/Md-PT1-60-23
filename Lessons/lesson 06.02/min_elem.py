l = [5,3,12,2,5,7,65,3,3,-1,56,8,6,4,3]

m = 0

for i in range(1, len(l)):
    if l[i] <= l[m]:
        m = i

print(m, l[m])

i = 0

while i<5:
    i+=1
    print(i)

l = [1,2,3,4,5,6,7]
i = 0
if True:
    while i < len(l):
        if i>-1:
            print(l[i])
            i+=1

for test_elem in l:
    print(test_elem)

print(test_elem)

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    for j in i:
        print(j)
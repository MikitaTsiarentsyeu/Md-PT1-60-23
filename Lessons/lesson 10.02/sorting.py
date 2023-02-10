l = [2,1,5,3,4,8,6,7]

# l.sort()

s_l = sorted(l)
print(l)
print(s_l)

l = []
l.extend("test")
l.sort()
print(l)

l = ["Abc", "aac", "test"]
l.sort()
print(l)


l = [7,3,5,3,12,6,8,4,-1]

# for j in range(len(l)-1):
#     print(l)
#     for i in range(len(l)-j-1):
#         if l[i]>l[i+1]:
#             l[i+1], l[i] = l[i], l[i+1]

# print(l)


for min in range(len(l)-1):
    j = min
    for i in range(j+1,len(l)):
        if l[min]>l[i]:
            min = i
        l[j], l[min] = l[min], l[j]
    print(l)
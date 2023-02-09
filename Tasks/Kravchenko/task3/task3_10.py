s = input().split()
l = []
l2 = []
for n in s:
    n = int(n)
    l.append(n)

for i in l:
    if i > 2:
        j = 2
        while i % j != 0 and j < i:
            j += 1
            if j == i:
                l2.append(i)
    elif i <= 2:
        l2.append(i)

m = 0
for value in l2:
    if value >= m:
        m = value
print(m)  


# one more solution:

# s = input().split()
# l = []
# l2 = []
# for i in s:
#     i = int(i)
#     l.append(i)

# for value in l:
#     for j in range(2,value):
#         if value % j == 0:
#             l2.append(value)
#             break

# s1 = set(l)
# s2 = set(l2)
# s3 = s1.difference(s2)


# m = 0
# for val in s3:
#     if val >= m:
#         m = val
# print(m)


#and one more:

# s = input().split()
# l = []
# for i in s:
#     i = int(i)
#     l.append(i)

# i = 0
# a = len(l) 
# while i < a:
#     y = 0
#     for j in range(2,l[i]):
#         if l[i] % j == 0:
#             y = 1
#             del l[i]
#             a = a - 1
#             break
#     if y == 0:
#         i += 1

# i = 0
# m = l[0]
# for l[i] in l:
#     if l[i] >= m:
#         m = l[i]
# print(m)
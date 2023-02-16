l = input('enter a string\n')
l = l.split()
d = {}

for i in l:
    n = 0
    for j in l:
        if i == j:
            n += 1
    d[i] = n
print(d)

# the second way:
# for i in l:
#     if i in d:
#         d[i] += 1
#         continue
#     d[i] = 1
# print(d)

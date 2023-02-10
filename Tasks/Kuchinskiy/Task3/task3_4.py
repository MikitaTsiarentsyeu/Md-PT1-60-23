l = input('enter a list of numbers separated by a space\n')
l = l.split()
l = list(dict.fromkeys(l))

for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        l[j] = int(l[j])
        l[j+1] = int(l[j+1])
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l[len(l)-2])


# finds the second smallest number:
# new_l = []
# m = 0

# for i in range(1,len(l)):
#     if l[i] < l[m]:
#         m = i

# for i in range(len(l)):
#     if l[i] == l[m]:
#         continue
#     new_l.append(l[i])

# n = 0

# for i in range(1,len(new_l)):
#     if new_l[i] < new_l[n]:
#         n = i

# print(new_l[n])
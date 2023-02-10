l = input('enter a string\n')
l = l.split()

l_new = []

for i in l:
    if len(i) > 5:
        l_new.append(i)
print(l_new)
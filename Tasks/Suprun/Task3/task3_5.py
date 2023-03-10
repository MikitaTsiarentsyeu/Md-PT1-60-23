string = input ("Enter any string:\n")
l = list(string.split(' '))
m = []
for elem in l:
    if len(elem) > 5:
        m.append(elem)
print(m)

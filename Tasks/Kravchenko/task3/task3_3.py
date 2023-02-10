t = input()
d = {}
t = t.lower().split()
for i in t:
    n = t.count(i)
    d[i] = n
print(d)

    
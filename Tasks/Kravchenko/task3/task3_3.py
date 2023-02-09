t = input()
d = {}
t = t.lower().split()
print(t)
print(t.count('a'))
for i in t:
    n = t.count(i)
    d[i] = n
print(d)

    
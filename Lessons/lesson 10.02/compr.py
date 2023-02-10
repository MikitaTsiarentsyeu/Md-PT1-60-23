print([x for x in range(10)])

l = [str(x) for x in range(10)]
print(l)

l = []
for x in range(10):
    if x%2 == 0:
        if x!=0:
            l.append(str(x))
print(l)

l = [chr(x**2) for x in range(10) if x%2==0 or x%3==0]
print(l)

d = {1:"one", 2:"two"}
l = [f"{k}:{v}" for k, v in d.items()]

print(l)

l = {x for x in "test string for set"}
print(l)

l = tuple(x for x in "test string for set")
print(l)

l = {x:chr(x*10) for x in range(1, 11)}
print(l)

l = [[1,2,3], [4,5,6], [7,8,9]]
print([f"{y}" for x in l for y in x])

k = []
for x in l:
    for y in x:
        k.append(str(y))
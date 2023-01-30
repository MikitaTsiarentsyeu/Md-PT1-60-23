l = []
print(type(l), len(l), l)

l = [1,2,3,4,5,'test',[6,7,8,9,10]]
print(l)

print(l[0], l[-1], l[1:3])

print(list("my test str"))

print([1,2,3]+[4,5,6])
print([0]*8)

l[0] = "1"
print(l)

# l[100] = "new elem" error
l.append("new elem")
print(l)
l.insert(0, 0.0)
print(l)
l.extend("test")
print(l)

l.remove("test")
print(l)

print(l.pop())
print(l.pop())
print(l.pop(0))
print(l.pop(0))
print(l)

del l[0]
print(l)

del l[:4]
print(l)

# del l
l.clear()
print(l)

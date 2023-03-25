l = []

l.append(0)
l[0] = '0'
l.remove('0')
print(l)

t = (1,2,3,4,5)
print(t, type(t))

t = ()
print(t, type(t))

t = (1, )
print(t, type(t))

t = 1,2,3,4,5
print(t, type(t))

t = (1,2,3,"four",5.0)

print(tuple("test str"))

print(t[0])

print((1,2,3)+(4,5,6))

# t[0] = 1.0 error
# t.append(1) error

del t

s = {1,2,3,4,5}
print(s, type(s))

s = set()
print(s, type(s))

s = set("test str")
s = ''.join(s)
print(s)

s = set([1,3,2,6,4,7,4,3,2,45,7,8,5,34,2,4,56,7,5,3])
s = list(s)
print(s)

s = {1,2,3,4,5}
s.add(6)
s.add(6)
s.add(6)
print(s)

s.update([4,5,6,7,8])
print(s)

s.remove(6)
print(s)

s.discard(6)
print(s)

coll1 = "test"
coll2 = ['t', 's', 'e']

print(set(coll1) == set(coll2))

print({1,2,3}.issubset({0,1,2,3,4,5,6,7,8,9}))
print(set(coll1).issubset(set(coll2)))
print(set(coll2).issubset(set(coll1)))
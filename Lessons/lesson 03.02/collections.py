d = {"one":1, "two":[2]}

key = 1
if key in d:
    print(d[key])
else:
    print(f"cannot find {key}")

res = d.get(key, f"cannot find {key}")
print(res)

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

if key in d.values():
    print("found it!")

# del d[key] error

# print(d.pop("two"))
print(d.popitem())

d.clear()
print(d)



t = (1,2,3,4,5)
print(type(t), t)

t = ()
print(type(t), t)

t = (1,)
print(type(t), t)

t = (1,2,3,"four",[])
print(t)

print(t[0])
# t[0] = 1.0 error

# del t[0]

l = list(t)
l[0] = 1.0
t = tuple(l)
print(t)




s = set()
print(type(s), s)


s = {1,2,3,4,5}
s.add(1)
s.add("test")
print(s)

s.update("test")
print(s)

s.remove("test")
print(s)

if "test" in s:
    s.remove("test")

s.discard("test")

print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))

s = "test"
s = set(s)
print(s)

l = list("test")
l = set(l)
l = list(l)
print(l)

a, b = "test", "set"
print(a == b)
print(set(a) == set(b))
print(set(a), set(b))


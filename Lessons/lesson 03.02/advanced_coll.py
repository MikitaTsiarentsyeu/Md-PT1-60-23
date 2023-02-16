print("test"=="set")

print([1,2,3] == [3,2,1])
print(set([1,2,3]) == set([3,2,1]))

l = [1,2,3]
l[0], l[1] = l[1], l[0]
print(l)

l = [[1,2,3], [4,5,6], [7,8,9]]
print(l)

print(l[0], l[1], l[2])

print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

t = (l, "test")
t[0][0][0] = 1.0
print(t)

# s = set(t) error

d = {"one":1}
d[(1,2,3)] = "1-2-3"
print(d)

# d[t] = "tuple" error

print({1,2,3}&{3,4,5})
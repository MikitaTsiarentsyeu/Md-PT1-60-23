from functools import reduce

(lambda x=2, y=3: x+y)()

def apply(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    apply(l, f, i+1)

def sq(x):
    print(x*x)

sq = lambda x: print(x*x)

# apply([1,2,3,4,5], sq)
apply([1,2,3,4,5], lambda x: print(x*x))

s = "abc Abc Aac aaa"
print(sorted(s.split(), key=lambda x: x.lower()))
print(sorted(s.split(), key=str.lower))

l = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda num: chr(num*10), l)))
# print(list(map(print, l)))

# print(list(filter(lambda x: x>2, l)))

print(list(map(lambda num: chr(num*10), filter(lambda x: x>5, l))))

print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: f"{x}-{y}", l))
print(reduce(lambda x, y: x if x>y else y, l))
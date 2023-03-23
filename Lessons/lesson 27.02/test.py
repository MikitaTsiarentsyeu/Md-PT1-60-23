def func(*args):
    for i in args:
        print(i)


l = [1,2,3,4,5]
func(*l, *[5,4,3,2,1], *"test")

l = [3,2,5,67,4,3,12]
# l.sort()
# print(l)
print(sorted(l))
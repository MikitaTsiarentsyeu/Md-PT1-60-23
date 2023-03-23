x = range(100)
print(x, type(x))

def bad_generator():
    yield 1
    yield 2
    yield 3.0
    yield "test"

# for i in bad_generator():
#     print(i)

gen1 = bad_generator()
gen2 = bad_generator()

print(gen1, type(gen1))

try:
    i = iter(gen1)
    while True:
        print(next(i))
except StopIteration:
    print("the end of iteration")

i = iter(gen2)
print(next(i))

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1
        if count == n:
            break
        a, b = b, a + b

l = [32,5,6,7,[45432,12,[1,45,3,2,5,78],4,2,65],6,42,4]

def flat_sum(l):
    total = 0
    for item in l:
        if isinstance(item, list):
            total += flat_sum(item)
        else:
            total += item
    return total

print(flat_sum([1, [2, [3], [4, [5] ] ] ]))


def flatten(l):
    for item in l:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

for i in flatten([1, [2, [3], [4, [5] ] ] ]):
    print(i)


def even_cubes(n):
    for i in n:
        if i % 2 == 0:
            yield i**3

even_cubes = (i**3 for i in range(10) if i % 2 == 0)

for i in even_cubes:
    print(i)

print(even_cubes)
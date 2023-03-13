def cache(func):
    d = {}
    def wrapper(*args):
        if args in d:
            return d[args]
        val = func(*args)
        d[args] = val
        return val
    return wrapper



@cache
def sum(a, b):
    return a + b

print(sum(2, 4))
print(sum(2, 4))
print(sum(3, 7))

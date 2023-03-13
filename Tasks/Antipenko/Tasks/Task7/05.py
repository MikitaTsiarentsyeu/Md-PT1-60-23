'''Write a decorator function that caches the return value of a function with a dictionary.
If the function is called again with the same arguments, return the cached value instead of computing it again.'''


def cachex(func):
    cache = {}

    def wrapper(*args):
        key = "_".join(str(x) for x in args)
        if key in cache:
            return cache[key]
        else:
            res = func(*args)
            cache[key] = res

        return res

    return wrapper


@cachex
def sdf(a, b):
    return a + b


sdf(2, 4)
sdf(3, 6)
sdf(3, 8)
sdf(2, 4)
sdf(1, 2)
sdf(2, 4)
sdf(2, 45)

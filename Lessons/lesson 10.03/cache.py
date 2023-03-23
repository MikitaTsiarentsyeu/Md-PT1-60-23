cache_position = 1

def cached(func):
    cache_position = 2
    def wrapper():
        cache_position = 3
        func()
    return wrapper

@cached
def sum(a, b):
    return a+b

@cached
def mult(a, b):
    return a*b

sum(2, 3)

mult(2, 3)
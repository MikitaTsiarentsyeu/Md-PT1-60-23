# 5. Write a decorator function that caches the return value of a function 
# with a dictionary. If the function is called again with the same arguments, 
# return the cached value instead of computing it again.


def cached(func):
    cache = {}
    
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        value = cache.get(key)
        if value is None:
            value = func(*args, **kwargs)
            cache[key] = value 
        return value
    return wrapper

@cached
def sum(a,b):
    res = a + b
    return res

print(sum(5,7))
print(sum(2,3))
print(sum(4,5))
print(sum(5,7))

@cached
def kwargs_processor(**kwargs): 
    s = ""
    for k, v in kwargs.items(): 
        s = (f'Key={k} and Value={v}')
        print(s)
    return s 

  
kwargs_processor(**{"name": 'Pankaj', "age":34} ) 
kwargs_processor(**{"name": 'Pankaj'} ) 
kwargs_processor(**{"name": 'Pankaj', "age":34} ) 

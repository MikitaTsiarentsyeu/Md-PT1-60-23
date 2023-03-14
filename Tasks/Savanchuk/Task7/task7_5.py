#5. Write a decorator function that caches the 
#return value of a function with a dictionary. 
#If the function is called again with the same arguments, 
#return the cached value instead of computing it again.
def cashing(func):
    dict = {}
    def wrapper(*args):
        res = func(*args)      
        if args in dict.keys():    # если 25, 19 уже в кэш
            return dict[args]     # вернуть значение из кэш
        else:
            dict[args] = res  # иначе знач 25, 19 присвоить 44 и добавить в кэш
            return res

    return wrapper
@cashing
def sum(a, b):
    return a + b
print(sum(25, 19))



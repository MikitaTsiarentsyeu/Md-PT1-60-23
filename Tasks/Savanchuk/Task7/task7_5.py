#5. Write a decorator function that caches the 
#return value of a function with a dictionary. 
#If the function is called again with the same arguments, 
#return the cached value instead of computing it again.
def cashing(func):
    def wrapper(*args):
        dict = {}
        res = func(*args)
        if args in dict.keys():
            return dict[args]
        else:
            dict[args] = res
            return res

    return wrapper
@cashing
def sum(a, b):
    return a + b
print(sum(25, 19))


# def cached_values(func):
#     dct = {}
#     def wrapper(*args, **kwargs):
#         if args in dct.keys():
#             return dct[args]
#         else:
#             result = func(*args, **kwargs)
#             dct[args] = result
#             return result
#     return wrapper



# @cached_values
# def sum_func(a, b):
#     return a+b


# print(sum_func(5,20))
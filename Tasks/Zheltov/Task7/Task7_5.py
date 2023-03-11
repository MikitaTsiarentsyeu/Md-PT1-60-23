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
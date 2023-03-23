import pickle

try:
    with open("dic.pickle", 'rb') as f:
        dic = pickle.load(f)
except FileNotFoundError:
    dic = {}

def cache(func):
    def inner(*args):
        if args in dic:
            return dic.get(args)
        else:
            dic[args] = func(*args)
            with open("dic.pickle", 'wb') as f:
                pickle.dump(dic, f)
            return func(*args)
    return inner

@cache
def sum(x, y):
    return x + y

print(sum(8, 7))
print(dic)
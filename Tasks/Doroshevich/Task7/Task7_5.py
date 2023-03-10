d = {}


def cash_in_dict(func):
    def wrapper(*args):
        if str(args) + func.__name__ in d:
            return d[str(args) + func.__name__]
        else:
            d[str(args) + func.__name__] = func(*args)
            return func(*args)
    return wrapper


@cash_in_dict
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "You only need to use numbers"


@cash_in_dict
def summ(a, b):
    return a+b


print(div(14, 5), d)
print(summ(14, 5), d)
print(div(14, 2), d)
print(div(14, 8), d)
print(div(14, 5), d)

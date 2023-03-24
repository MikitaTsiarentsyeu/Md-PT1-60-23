'''Write a decorator function that logs the execution time, arguments and return value of a function to a file.'''

import datetime


def my_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = datetime.datetime.now()
        result = func(*args, **kwargs)
        time_end = datetime.datetime.now()
        time = time_end - time_start
        with open('cfile.txt', 'a') as f:
            f.write(f'Function "{func.__name__}" arguments: {args, kwargs}, return - {result}\n')
            f.write(f'Finished successfully in {time} seconds\n')
            f.write('--------------\n')
        return result

    return wrapper


@my_decorator
def calculate(num):
    total = sum((x for x in range(0, num ** 3)))
    return total


@my_decorator
def division(cum, li):
    divis = [cum * x for x in li]
    return divis


vv = ['re', 'ert', 'rtgedfbh']

print(calculate(500))
print(division(3, vv))

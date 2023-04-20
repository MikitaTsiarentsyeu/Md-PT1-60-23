import time
from functools import wraps

def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        ex_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {ex_time} секунд.')
        return result
    return wrapper

def cache_args(func):
    с = {}
    @wraps(func)
    def wrapper(*args):
        if args not in с: 
            с[args] = func(*args)
        return с[args]
    return wrapper

@time_check
@cache_args
def long_heavy(n1, n2):
    time.sleep(1)
    return n1 + n2
print(long_heavy(5, 9))
print(long_heavy(6, 2))
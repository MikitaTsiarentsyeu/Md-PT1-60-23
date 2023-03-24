import time
from functools import wraps

def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result
    return wrapper

def cache_args(func):
    dt = {}
    @wraps(func)
    def wrapper(*args):
        if args not in dt:  # При каждом вызове проверяйте, не было ли уже аналогичного вызова
            dt[args] = func(*args)
        return dt[args]
    return wrapper


@time_check
@cache_args
def long_heavy(n1, n2):
    time.sleep(1)
    return n1 + n2

print(long_heavy(1, 2))
print(long_heavy(1, 2))
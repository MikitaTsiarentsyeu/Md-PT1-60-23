def timemometr(func):
    from time import time
    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения функции {end_time-start_time} секунд')
        return value
    return wrapper
@timemometr
def summa(a, b):
    from time import sleep
    sleep(1)
    return a + b
print(summa(8,3))

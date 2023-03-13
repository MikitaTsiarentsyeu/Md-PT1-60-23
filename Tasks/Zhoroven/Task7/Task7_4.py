import time


def log_func(func):
    def wrapper(x, y):
        starttime = time.time()
        div = func(x, y)
        endtime = time.time() - starttime
        with open('Log.txt', 'w') as log:
            result = f" Делимое {x}\n Делитель {y}\n Результат {div}\n Время выполнения {endtime}"
            log.write(result)
        log.close
    return (wrapper)


@log_func
def devide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except:
        print("Error")


devide(1, 0)

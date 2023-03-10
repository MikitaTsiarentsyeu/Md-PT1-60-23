import time

def log_func(func):
    def wrapper(x,y):
        starttime = time.time()
        rez = func(x,y)
        endtime = time.time() - starttime #вне дебага выдает ноль, вероятно изза скорости выполнения
        with open('LogBook.txt','w') as log:
            rezult = f"Делимое = {x}\nДелитель = {y}\nЧастное = {rez}\nВремя выполнения = {endtime}"
            log.write(rezult)
        log.close
    return wrapper

@log_func
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except:
        return "Invalid data input"

divide(1,2)


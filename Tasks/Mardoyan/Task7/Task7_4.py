from datetime import datetime
def time_func(func):
    def log_func():
        start = datetime.now()
        result = func()
        finish = datetime.now()
        with open('new_file_with_values.txt','w',encoding='utf-8') as f:
            values = f' Время старта={start}\n Время завершения={finish}\n Время выполнения программы={finish - start}\n Значение={result} четных чисел' 
            f.write(values)
        return result
    return log_func
@time_func
def spis(): #Кол-во четных чисел
    a = 0
    for i in range(10000):
        if i % 2 == 0:
            a += 1
    return a
print(spis())


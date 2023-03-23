import time
import csv


def dec_res_in_file(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        ex_time = time.perf_counter() - start
        keys = ["function name", "execution time",
                "arguments", "keyword arguments", "result"]
        row = [func.__name__, ex_time, args, kwargs, res]
        try:
            with open('file.csv') as r:
                with open("file.csv", 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
        except FileNotFoundError:
            with open("file.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(keys)
                writer.writerow(row)
        return res
    return wrapper


@dec_res_in_file
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "You only need to use numbers"


@dec_res_in_file
def summ(a, b):
    return a+b


print(summ(14, 7))
# print(div(14, 7))
# print(summ(24, 456))
# print(summ(-10, 5))
# print(div(14, 0))
# print(div(24, 7))
# print(div(295, 13))
# print(summ(0, 7))

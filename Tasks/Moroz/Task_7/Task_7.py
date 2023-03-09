import time


# 1. Write a function that takes two numbers as input and returns their division.
# Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.


def division(num1: int, num2: int) -> int:
    try:
        return int(num1/num2) if num1 % num2 == 0 else round(num1/num2, 2)
    except ZeroDivisionError:
        print("You can't divide by 0")


print(division(True, 3))


# 2. Write a function that reads a file and returns its contents as a string.
# Handle the FileNotFoundError and return "File not found" if the file does not exist.

files_lst = ["text.txt", "another_text.txt", "whatever.txt"]

"""Checking 1 file that exists and failing to open the others"""
def file_reader(files_lst: list) -> str:
    for f in files_lst:
        try:
            with open(f) as file:
                lines = "".join("".join(file.readlines()))
                print(lines)
        except FileNotFoundError:
            print(f"{f} - file was not found")


file_reader(files_lst)


# 3. Write a function that takes a list of integers as input and returns the sum of all even numbers in the list.
# Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.

def sum_even_nums(my_lst: list) -> int:
    try:
        if isinstance(my_lst, list):
            new_lst = [i*(i % 2 == 0) if isinstance(i, int) else TypeError for i in my_lst]
            return sum(new_lst)
        else:
            raise TypeError

    except TypeError:
        return "Invalid input type"


print(sum_even_nums([20,21,44]))



# 4. Write a decorator function that logs the execution time,
# arguments and return value of a function to a file.



def log_func(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print(t1)
        outer_func = func(*args, **kwargs)
        t2 = time.time()
        print(t2)
        logs = {}
        logs["arguments"] = args
        logs["func_result"] = outer_func
        logs["timing"] = t2-t1
        with open("logs.txt", "w") as file:
            for line in logs.items():
                file.writelines(str(line)+'\n')
        return logs
    return wrapper

@log_func
def sum_func(a,b):
    return sum((x for x in range(0, (a+b)**2)))


print(sum_func(200, 5))



# 5. Write a decorator function that caches the return value of a function with a dictionary.
# If the function is called again with the same arguments, return the cached value instead of computing it again.



def cached_values(func):
    dct = {}
    def wrapper(*args, **kwargs):
        dct_key = (args, tuple(kwargs.items()))
        if dct_key not in dct.keys():
            result = func(*args, **kwargs)
            dct[dct_key] = result
        return dct[dct_key]
    return wrapper



@cached_values
def sum_func(a, b):
    return a+b


print(sum_func(5,20))



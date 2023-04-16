# 4. Write a decorator function that logs the execution time, 
# arguments and return value of a function to a file.

import time

def log(func):
    def wrapper(*args):
        start_time = time.time()
        val = func(*args)
        finish_time = time.time()
        time_execution = finish_time - start_time
        with open('myfile.txt', 'w', encoding='utf-8') as file:
            file.write(f"time execution is {time_execution} seconds\n")
            file.write(f"the function arguments are {args} \n")
            file.write(f"the function result is {val} \n")        
        return file
    return wrapper

@log
def sorting(list):
    sorted_numbers = sorted(list)
    return sorted_numbers
sorting([5,4,6,1,7,3])


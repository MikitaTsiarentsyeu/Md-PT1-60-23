from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now() - start
        with open('new_text.txt', 'a') as new:
            e = f'{end}'
            new.write(e)
        return result
    return wrapper 

@timeit
def even(n):
    l = [x for x in range(n+1) if x % 2 == 0]
    l = str(l)
    with open('new_text.txt', 'w') as new1:
            f = f'{l}\n'
            new1.write (f)
    return l

even(int(input("Enter your range to find all even numbers:\n")))
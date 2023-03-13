import time
def execution_time(funk):
    def wrapper():
        start = time.time()
        val = funk()
        end = time.time() - start
        with open("text.txt", 'w') as f:
            f.write(f'execution time {end},value of a function {val}')
        return val
    return wrapper

@execution_time
def sum_of_even_numbers():
    count = 0
    for i in range(1000000):
        if i % 2 == 0:
            count += i
    return count

print(sum_of_even_numbers())
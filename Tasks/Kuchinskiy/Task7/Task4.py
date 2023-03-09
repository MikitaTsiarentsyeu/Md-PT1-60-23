import time
# start = time.time()
# for i in range(100):
#     print(i)
# end = time.time() - start
# print(end)

def dec_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start
        with open("reg.txt", 'w') as f:
            f.write(f"execution time: {end}\narguments: {args} \nvalue: {func(*args, **kwargs)}")
    return inner

@dec_time
def hundred(s):
    for i in range(s):
        print(i)

hundred(100)
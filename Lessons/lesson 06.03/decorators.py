# def double_say_hello():
#     say_hello()
#     say_hello()

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def do_hundred(func):
    def wrapper():
        for i in range(100):
            func()
    return wrapper

@do_hundred
@do_twice
def say_hello():
    print("Hello!")


# say_hello = do_twice(say_hello)
# say_hello = do_hundred(say_hello)
# say_hello()


def comment(func):
    def wrapper(*args, **kwargs):
        print("the process is started")
        res = func(args[0], args[1])
        print("the process is finished")
        global args_count
        args_count = len(args)
        return res
    return wrapper

@comment
def sum(a, b):
    return a+b

@comment
def cross(a, b):
    return a*b

print(sum(3, 4))
print(cross(3, 4))


def test_sum(a, b):
    res = a+b
    return res

print(test_sum(2.2, 5))

def test_print(val):
    print(val)

test_print(test_sum(2.2, 5))

def my_func1():
    print("my func 1")
    my_func2()

def my_func2():
    print("my func 2")

my_func1()

def test(): pass
print(test, id(test), type(test))

test()


sign = "*"
# if sign == "+":
#     def oper(a, b):
#         return a+b
# elif sign == "*":
#     def oper(a, b):
#         return a*b
    
def oper(a, b, sign):
    if sign == "+":
        return a+b
    elif sign == "*":
        return a*b


print(oper(3, 7, "+"))


def order(x, y):
    print(id(x), id(y))
    x.append("3")
    y.append(8)
    print(id(x), id(y))
    print(f"{x} {y}")

x, y = ["x"], ["y"]
print(id(x), id(y))
order(x, y)
print(x, y)

mpv = print
mpv("my new print ref")

def test_return():
    print("after return")

print(test_return())

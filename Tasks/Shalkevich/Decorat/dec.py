from datetime import datetime


def time(fun):
    def now():
        Start = datetime.now()
        most = fun()
        print(datetime.now() - Start)
        return most
    return now


@time
def ones():
    Even = []
    for i in range(10 ** 4):
        if i % 2 == 0:
            Even.append(i)
    return Even


@time
def two():
    NoEven = []
    for i in range(10 ** 4):
        if i % 2 == 1:
            NoEven.append(i)
    return NoEven


even = ones()
Noeven = two()

print(even, '\n', Noeven)

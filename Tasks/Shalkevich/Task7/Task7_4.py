from datetime import datetime


def time(fun):
    def now():
        Start = datetime.now()
        most = fun()
        end = datetime.now() - Start
        with open('txt.txt', 'w') as  txt:
            z = f'время начала ={Start}, "\n значения ={most},"\n время выполнения = {end}'
            txt.write (z)
        return most
    return now

@time
def ones():
    Even = []
    for i in range(10 ** 4):
        if i % 2 == 0:
            Even.append(i)
    return Even

print(ones())
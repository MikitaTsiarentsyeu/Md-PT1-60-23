#Функция возвращает куб числа


def first_func(func):
    cube = {}
    def inner(*args):
        if args[0] in cube:
            return cube[args[0]]
        z = func(args[0])
        cube[args[0]] = z
        print(cube)
        return z
    return inner

@first_func
def cube_math(q):
    return q ** 3
try:
    print(cube_math(int(input('Введите число,куб которого хотели бы узнать!'))))
except IndexError:
    print('Я же попросил число!')

        
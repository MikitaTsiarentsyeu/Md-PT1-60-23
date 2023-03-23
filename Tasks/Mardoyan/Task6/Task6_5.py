def fact(a):
    if a == 1:
        return 0
    if a == 2:
        return 1
    return fact(a-1)+fact(a-2)
x = int(input('Input number\n'))
print(fact(x))
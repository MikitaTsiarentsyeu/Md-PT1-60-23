step = 1
def pow_func(a,b):
    global step
    if b == 1:
        return step*a
    else:
        step = a*step
    return pow_func(a,b-1)
x = int(input('Input number\n'))
d = int(input('Input power\n'))
print(pow_func(x,d))
def power(arg, deg):
    if deg == 1:
        return arg
    return arg * power(arg, deg-1)

print(power(2,8))
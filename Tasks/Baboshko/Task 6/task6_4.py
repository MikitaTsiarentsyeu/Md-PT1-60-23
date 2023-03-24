def power(x, y):
    if y != 0:
        return x * power(x, y-1)
    else:
        return 1
print(power(int(input()), int(input())))
def power_num(num, exponent):
    if exponent == 0:
        return 1
    return num * power_num(num, exponent - 1)


print(power_num(8, 2))

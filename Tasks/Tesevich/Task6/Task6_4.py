def power_func(number, power):
    if power == 1:
        return number
    else:
        return power_func((number*number),(power - 1))

print(power_func(4,4))

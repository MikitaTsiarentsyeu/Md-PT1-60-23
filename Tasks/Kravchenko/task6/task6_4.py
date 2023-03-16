number = int(input('Input a number\n'))
power = int(input('Input power\n'))
def calc_power(power):
    if power == 0:
        return 1
    return number * calc_power(power - 1)
print(calc_power(power))

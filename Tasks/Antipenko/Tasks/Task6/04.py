'''4. Write a recursive function to calculate the power of a given number.'''


def power_of_number(number, rate):
    if rate == 1 or number < 2:
        return number

    return number * power_of_number(number, rate - 1)


print(power_of_number(8, 4))

def power_of_number(n, p):
    if p == 1:
        return n
    return n * power_of_number(n, p - 1)
print(power_of_number(5, 2))
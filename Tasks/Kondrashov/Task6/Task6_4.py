def recursive_numb_power(numb, power):
    if power == 1:
        return numb
    else:
        return numb * recursive_numb_power(numb, (power - 1))

print(recursive_numb_power(numb=int(input('Введите число:\n')),
                           power=int(input('Введите степень:\n'))))
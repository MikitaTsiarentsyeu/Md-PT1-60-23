def num_func(num):
    x = str(num[0])
    for i in range(len(num) - 1):
        if num[i] + 1 == num[i + 1]:
            if x[-1] != '-':
                x += '-'
            else:
                pass
        elif num[i] + 1 != num[i + 1]:
            if not f'{num[i]}' in x:
                x += f'{num[i]}, {num[i + 1]}'
            else:
                x += f', {num[i + 1]}'
    if x[-1] == '-':
        x += f'{num[-1]}'
    return x
print(num_func([1, 2, 3, 4, 7, 8, 10, 12, 13, 15]))

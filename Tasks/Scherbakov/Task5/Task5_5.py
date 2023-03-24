num = input('Enter your numbers with a "space":\n').split()
num = [int(i) for i in num]

def diapazon(a):
    a.sort()
    s = str(a[0])
    for i in range(len(a) - 1):
        if a[i] + 1 == a[i + 1]:
            if s[-1] != '-':
                s += '-'
            else:
                pass
        elif a[i] + 1 != a[i + 1]:
            if not f'{a[i]}' in s:
                s += f'{a[i]}, {a[i + 1]}'
            else:
                s += f', {a[i + 1]}'
    if s[-1] == '-':
        s += f'{a[-1]}'
    return f'Your number ranges are:\n{s}'

print(diapazon(num))

#

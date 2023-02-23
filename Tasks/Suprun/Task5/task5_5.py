num = input("Enter any numbers separeted by commas:\n")
num = {int(i) for i in num.split(',')}
num = list(num)
num.sort()

def get_ranges (l):
    ran = str(l[0])
    for i in range(len(l) - 1):
        if l[i] + 1 == l[i + 1]:
            if ran[-1] != '-':
                ran += '-'
        elif l[i] + 1 != l[i + 1]:
            if not f'{l[i]}' in ran:
                ran += f'{l[i]},{l[i + 1]}'
            else:
                ran += f',{l[i + 1]}'
    if ran[-1] == '-':
        ran += f'{l[-1]}'

    return ran
print(get_ranges(num))


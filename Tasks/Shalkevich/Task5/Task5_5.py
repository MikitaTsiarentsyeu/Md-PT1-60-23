def nombers (nom):
    x = str(nom[0])
    for i in range(len(nom) - 1):
        if nom[i] + 1 == nom[i + 1]:
            if x[-1] != '-':
                x += '-'
            else:
                pass
        elif nom[i] + 1 != nom[i + 1]:
            if not f'{nom[i]}' in x:
                x += f'{nom[i]}, {nom[i + 1]}'
            else:
                x += f', {nom[i + 1]}'
    if x[-1] == '-':
        x += f'{nom[-1]}'
    return x
print(nombers([1, 2, 3, 4, 7, 8, 10, 12, 13, 15]))

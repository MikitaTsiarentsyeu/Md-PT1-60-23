string = str(input('Введите любые символы:\n'))
d = {'Спец.символы': 0, 'Буквы': 0, 'Цифры': 0}
q = {}
for i in string:
    if i.isalpha():
        d['Буквы'] += 1
    elif i.isdigit():
        d['Цифры'] += 1
    else:
        d['Спец.символы'] += 1

for char in set(string):

    q[char] = string.count(char)

print(f'Цифры:{d["Цифры"]}\nБуквы:{d["Буквы"]}\nСпец.символы:{d["Спец.символы"]}')
print(q)

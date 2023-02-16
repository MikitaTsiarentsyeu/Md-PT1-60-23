text = input("Введите любое слово:\n")
x = ('а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я')

for letter in text:
    if letter not in x:
        print(letter, end='')
    
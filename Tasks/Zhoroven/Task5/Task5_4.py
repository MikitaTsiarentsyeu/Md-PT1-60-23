

def count_Upper_lower_symbols(string):
    UPPER_SYMBOLS = ('QWERTYUIOPLKJHGFDSAZXCVBNM')
    LOWEL_SYMBOLS = ('qwertyuioplkjhgfdsazxcvbnm')
    upper = 0
    lowel = 0
    for i in string:
        if i in UPPER_SYMBOLS:
            upper += 1
        elif i in string:
            if i in LOWEL_SYMBOLS:
                lowel += 1

    return print(f'Lowel symbols is {lowel}\nUpper symbols is {upper}')


count_Upper_lower_symbols(string=('How Many Upper and Lowel Symbols?'))

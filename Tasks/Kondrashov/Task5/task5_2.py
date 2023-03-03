def revers_string():
    text = input()
    rev_string = []
    for i in text:
        rev_string += i
    print(''.join(reversed(rev_string)))


revers_string()

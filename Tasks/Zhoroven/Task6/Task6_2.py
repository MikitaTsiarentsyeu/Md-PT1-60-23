def palidrome_str(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palidrome_str(text[1:-1])


print(palidrome_str('lol'))

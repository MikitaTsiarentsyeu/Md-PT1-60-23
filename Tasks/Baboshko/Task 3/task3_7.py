text_string = input('Пожалуйста, введите строку с заглавными и строчными буквами: \n')
new_string = ''
for i in range(len(text_string)):
    if text_string[i].islower():
        new_string = new_string + text_string[i].upper()
    else:
        new_string = new_string + text_string[i].lower()
print(new_string, text_string.swapcase(), sep = '\n')#swapcase быстрее, конечно)
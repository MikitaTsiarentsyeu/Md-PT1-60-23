text_string = input('Пожалуйста, введите строку кирилицей: \n')
new_string= ''
for i in range(len(text_string)):
    if text_string[i] in 'ёуеыаоэяию':
        continue
    else:
        new_string = new_string + text_string[i]
print(new_string)
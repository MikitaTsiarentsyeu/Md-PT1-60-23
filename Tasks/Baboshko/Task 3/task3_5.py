text_string = input('Пожалуйста, введите любое количество строк: \n').split()
string_5 = []
for i in range(len(text_string)):
    if len(text_string[i]) > 5:
        string_5.append(text_string[i])
print(string_5)
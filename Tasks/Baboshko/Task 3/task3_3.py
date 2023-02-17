new_str = input('введите строку, пожалуйста: \n').split()
dict_words = {}
for i in range(len(new_str)):
    dict_words[len(new_str[i])] = new_str[i]
print(dict_words)
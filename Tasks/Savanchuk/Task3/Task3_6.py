list = input("Введите Ваше предложение.\n")

new_list = ""
vowels = ["а", "о", "у", "ы", "э", "и", "е", "ё", "ю", "я"]
for i in list:
    if i.isalpha():    # проверяет строка, чтоб состояла из бкувенных символов
        if i.lower() not in vowels:
            new_list += i 
print(new_list)
# не совсем правильно работает, нужно переделать !
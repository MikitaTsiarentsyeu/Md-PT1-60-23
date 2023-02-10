answer = input("Введите Ваше предложение.\n")
vowels = ["а", "о", "у", "ы", "э", "и", "е", "ё", "ю", "я"]
count = 0 #счетчик
for i in answer.lower():
    if i.isalpha():    # проверяет строка, чтоб состояла из бкувенных символов
        if i in vowels:
            count += 1
print (count) 

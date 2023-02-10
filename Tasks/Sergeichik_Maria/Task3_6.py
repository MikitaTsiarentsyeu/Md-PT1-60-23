smth = input("Введите произвольную строку: \n")
newWord = ''
sss = ['а' , 'я' , 'у' , 'ю' , 'о' , 'е' , 'ё' , 'э' , 'и' , 'ы']
for i in smth:
    if i.lower() not in sss:
        newWord += i
print (newWord)        
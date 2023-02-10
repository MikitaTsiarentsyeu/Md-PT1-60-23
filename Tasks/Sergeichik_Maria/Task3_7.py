yWord = input("введите ваше предложение: \n")
newWord = ''
words = yWord.split(" ")
for i in words:
    if i.isupper():
        newWord += i + " "
        print(newWord.lower())
    elif i.islower():
        newWord += i + " "
        print(newWord.upper())
print("Привет, ты знаешь гласные буквы? Напиши мне что-нибудь и я найду все гласные буквы")
Text = input()
vowels = 0
consonants = 0
text = ''
vowel = ''
cons = ''
for i in Text:
    if i.isalpha():
        text = ''.join([text, i])

for i in text:
    letter = i.lower()
    if  letter == "a" or letter == "e" or\
        letter == "i" or letter == "o" or\
        letter == "u" or letter == "y" or\
        letter == "а" or letter == "о" or\
        letter == "я" or letter == "у" or\
        letter == "ю" or letter == "е" or\
        letter == "ё" or letter == "э" or \
        letter == "и" or letter == "ы":
        vowels += 1
        vowel = ''.join([vowel, i])
    else:
        consonants += 1
        cons = ''.join([cons, i])
print("гласных %i\nсогласных %i" % (vowels, consonants),"\n гласные\ согласные \n", vowel , cons)


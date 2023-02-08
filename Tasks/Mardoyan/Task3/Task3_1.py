print('Hello! I can help you count the vowels in your string.')
x = input('Input you string(on English)\n')
vowels = 0
for i in x:
    letter = i.lower()
    if letter == "a" or letter == "i" or\
       letter == "u" or letter == "e" or\
       letter == "y" or letter == "o":
       vowels += 1
print(vowels)
        
print('Hello!I can return the string with all vowels removed.')
x = input('Input you string(on English)\n')
b =''
for i in x:
    letter = i.lower()
    if letter != "a" and letter != "i" and\
       letter != "u" and letter != "e" and\
       letter != "y" and letter != "o":
       b += letter
print(b)  
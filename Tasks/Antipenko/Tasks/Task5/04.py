''' Write a function that takes a string as an argument and returns two numbers, first for count of
lower case symbols, second for count of the upper case symbols in the initial string. '''

def register(s):
    a=0
    b=0
    for i in s:
        if i.islower():
            a+=1
        elif i.isupper():
            b+=1
        else: continue
    return f'Lower characters - {a}, top characters - {b}, other characters or digits - {len(s)-a-b}'

df='sf;oijpKOPDks;K?lvcIDF;Ix<329IF >ed'
print(register(df))

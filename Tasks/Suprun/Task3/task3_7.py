string  = input("I can convert all capital letters to lowercase and vice versa.\nEnter any string:\n")
new_string = ''
for i in string:
    if i.isupper():
        new_string += i.lower()
    else:
        new_string += i.upper()
print(new_string)
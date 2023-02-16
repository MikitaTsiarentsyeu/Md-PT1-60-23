your_string = input('Please, input your string:\n')
inverse_string=''
for i in your_string:
    inverse_string+= i.lower() if i.isupper() else i.upper()
print(inverse_string)
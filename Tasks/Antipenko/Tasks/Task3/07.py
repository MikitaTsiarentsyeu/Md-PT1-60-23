""" Write a program that takes a string as input and returns the string
with all capital letters converted to lowercase and vice versa."""

your_string = input('Please, input your string:\n')

inverse_string=''

for i in your_string:
    inverse_string+= i.lower() if i.isupper() else i.upper()

print(inverse_string)
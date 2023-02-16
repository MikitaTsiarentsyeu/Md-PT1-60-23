# Write a program that takes a string as input and returns the string reversed.

your_string = input('Please, input your string:\n')

reversed_string=''
for symbol in your_string:
    reversed_string=symbol+reversed_string
print(reversed_string)
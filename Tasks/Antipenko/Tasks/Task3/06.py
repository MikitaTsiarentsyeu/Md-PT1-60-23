# Write a program that takes a string as input and returns the string with all vowels removed.

your_string = input('Please, input your string:\n')

vowels = 'aeiouy'
string_without_vowels=''

for i in your_string:
    if i in vowels:
        continue
    else:
        string_without_vowels+=i
print(string_without_vowels)
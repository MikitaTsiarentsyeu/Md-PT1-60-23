# Write a program that takes a string as input from a user and returns the number of vowels in the string.

your_string = input('Please, input your string:\n')

vowels = 'aeiouy'
l = 0

for i in your_string:
    if i in vowels:
        l += 1
print(l)

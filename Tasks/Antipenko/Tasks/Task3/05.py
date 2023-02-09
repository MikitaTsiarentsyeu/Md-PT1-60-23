"""Write a program that takes a list of strings as input and returns a list
with all strings that have a length greater than 5 characters."""

list_of_strings = input('Enter numbers separated by spaces:\n').split()

list_5_char=[]
for i in list_of_strings:
    if len(i)>5:
        list_5_char.append(i)
print(list_5_char)
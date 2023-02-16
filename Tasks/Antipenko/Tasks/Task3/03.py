# Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
list_of_words = input('Enter your string:\n').split()

new_dict = {}
number=1
for word in list_of_words:
    new_dict[number] = word
    number+=1
print(new_dict)
list_of_words = input('Enter your string:\n').split()
first_dict = {}
number=1
for word in list_of_words:
    first_dict[number] = word
    number+=1
print(first_dict)
string = input("Enter some words and I'll delete all vowels from it:\n")
vowels = ('a', 'e', 'i', 'o', 'u', 'y', "а", "е", "ё", "и", "о", "у", "э", "ю", "я", "ы")
string = string.lower()
for i in vowels:
    string = string.replace(i, '')
print(string)
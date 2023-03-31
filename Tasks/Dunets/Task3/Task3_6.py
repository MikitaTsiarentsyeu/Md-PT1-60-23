text = list(input("Please, write a random text in any format:\n"))

new_text = []

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

for letter in text:
    if not letter in vowels:
        new_text.append(letter)

print("".join(new_text))

# On the weekends we all play board games together
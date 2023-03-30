text = input("Please, write a random text in any format:\n")  # Hello man! How are you?

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

vow = 0

for letter in text:
    if letter in vowels:
        vow += 1

print('The number of vowels is: ', vow)

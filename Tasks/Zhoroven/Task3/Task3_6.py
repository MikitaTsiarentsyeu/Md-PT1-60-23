num_words = int(input("Enter number words, where max = 3:\n"))

user_words = []
# vowels = 'aoeiu'

for i in range(1, num_words + 1):
    words = input("Enter word:\n")
    for vowel in 'aoeiu':
        words = words.replace(vowel, '')

    user_words.append(words)

if num_words == 1:
    print(f"Word without vowels:\n{user_words.pop(0)}")

elif num_words == 2:
    print(f"Words without vowels:\n{user_words.pop(0)}")
    print(user_words.pop(0))

elif num_words == 3:
    print(f"Words without vowels:\n{user_words.pop(0)}")
    print(user_words.pop(0))
    print(user_words.pop(0))

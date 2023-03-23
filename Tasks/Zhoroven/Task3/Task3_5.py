words_list = int(input("Enter number words:\n"))

user_list = []

for i in range(1, words_list + 1):
    words = input(" Enter word:\n")
    if len(words) >= 5:
        user_list.append(words)

print(f"List of words with 5 characters: {user_list}")

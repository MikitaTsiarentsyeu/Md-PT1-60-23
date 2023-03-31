user_words = input("Please, write any text in any format:\n").split()

new_list = []

for word in user_words:
    if len(word) > 5:
        new_list.append(word)

print(new_list)

# On the weekends we all play board games together
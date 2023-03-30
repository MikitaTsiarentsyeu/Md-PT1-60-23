user_words = input("Please, write any text in any format:\n").split()

count_words = {}

x = 1

for word in user_words:
    count_words[x] = word
    x += 1

print(count_words)
print("Number of words in dictionary is", max(count_words))

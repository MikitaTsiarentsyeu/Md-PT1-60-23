words = input(" Enter any words:\n")

words_list = list(words.split(' '))
print(words_list)

scores = {index: elem for index, elem in enumerate(words_list)}

print(scores)

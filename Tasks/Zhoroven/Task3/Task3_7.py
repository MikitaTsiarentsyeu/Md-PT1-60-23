user_words = input("Enter word with CAPITAL letters:\n")

user_words.split(" ")
capital_words = user_words

capital_letters = "ZXCVBNMLKJHGFDSAQWERTYUIOP"
lovercase_letters = "zxcvbnmlkjhgfdsaqwertyuiop"


for i in user_words:
    if i in capital_letters:
        user_words = user_words.casefold()
        continue

for i in capital_words:
    if i in lovercase_letters:
        capital_words = user_words.capitalize()

        break

print(
    f"Words with lowelcase letters:{user_words}\nWords with capital letters {capital_words}")

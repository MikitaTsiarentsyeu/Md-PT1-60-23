text = list(input("Please, write a random text in any format:\n"))

new_text = []

i = len(text)

while i > 0:
    new_text += text[i - 1]
    i = i - 1

print("".join(new_text))

# On the weekends we all play board games together
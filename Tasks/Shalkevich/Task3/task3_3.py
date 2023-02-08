print("Здравствуй пользователь великих технологий, пришло время проверить сколько слов ты можешь написать!")
Text = input("Давай.. не ограничивай себя")
strin = {}
for i in Text:
    strin = Text.split()

print(len(strin), strin)
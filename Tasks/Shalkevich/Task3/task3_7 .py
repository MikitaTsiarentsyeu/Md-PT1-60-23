print("Здраствуйте, чего бы вы хотели?")
answer = input()
answ = ''
for i in answer:
    if i == i.upper():
        answ += i.lower()
    elif i == i.lower():
        answ += i.upper()
print(answ)
def upLow(Text):
    text = {'up' : 0, 'lo' : 0}
    for i in Text:
        if i.isupper():
            text['up']+=1
        elif i.islower():
            text['lo']+=1
        else: pass
    return print ("Ваш текст",Text, "из них большие", text["up"], "из них маленькие", text["lo"])

upLow(input("Напиши мне что-нибудь"))


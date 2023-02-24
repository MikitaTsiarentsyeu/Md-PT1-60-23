def revers(Text):
    Text = Text.split()
    for i in Text:
        if len(i) > 4:
            print(i)
    return


revers(input("Напиши мне что-нибудь"))

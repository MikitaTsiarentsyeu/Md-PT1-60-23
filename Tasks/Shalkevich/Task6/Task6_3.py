def Whatis(What, leters = 0):
    if What == "":
        return leters, "столько буквы вы ввели"
    elif What.isalpha():
        return Whatis(What[1:],leters + 1)

while True:
    text = input("что-то с чем-то")
    print(Whatis(text))

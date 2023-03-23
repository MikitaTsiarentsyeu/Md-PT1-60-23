def stri(mes):
    if len(mes) == 1:
        return mes
    return mes[-1] + stri(mes[:-1])

while True:
    stro = input("что-то")
    stro.split()
    print(stri(stro))
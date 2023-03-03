def Wot(numb, po):
    if po == 1:
        return numb
    else:
        return numb * Wot(numb, (po - 1))

while True:
    nom,st = int(input("что-то считаем?")), int(input("В какую степень возводим?"))
    print(Wot(nom, st))

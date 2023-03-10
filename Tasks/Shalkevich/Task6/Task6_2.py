def poliandros (pol):
    if len(pol) < 1:
        return True
    else:
        if pol[0] == pol[-1]:
            return poliandros(pol[1:-1])
        else:
            return False
while True:
    What = input("что-то с чем-то)")
    if poliandros(What):
        print("Полиандрус!")
    else:
        print("Фейковый палиндрус!")
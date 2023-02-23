
c = input(f"Введите строчку\n")


def uantity (c1):
    nUP = 0 
    nD = 0 
    
    for i in c1:
        if 90 >= ord(i) >= 65:
            nUP += 1      
        elif 122 >= ord(i) >= 97:
            nD += 1 
            

    return nUP, nD

print(uantity(c))



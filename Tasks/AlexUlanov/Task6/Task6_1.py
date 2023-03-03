a = input("Введите строчку. Будет переворот строки\n")


def OpposideDown(a, st1=""):
    if len(a)==0:        
        return st1
    st1 += str(a[-1]) 
    
    return OpposideDown(a[:-1], st1)


print(OpposideDown(a))






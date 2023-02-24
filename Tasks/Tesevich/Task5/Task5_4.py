def UpDo(a):
    tit = 0
    lit = 0
    a = list(a)
    for x in a:
        if x.istitle():
            tit = tit +1
        elif x.islower():
            lit = lit +1
    return(lit, tit)
        
print(UpDo((input('Input your list:\n'))))
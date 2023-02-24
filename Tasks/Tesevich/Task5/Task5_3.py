def dlin(a):
    x2= []       
    a = a.split(" ")
    for x in a:
        if len(x) >=5:
            x2.append(x)
    return(x2)
        
print(dlin((input('Input your list:\n'))))

def revers1(a):
    x2= []       
    a = a.split(" ")
    a = reversed(a)
    for x in a:
        x1 = "".join(reversed(x))
        x2.append(x1)
    return(x2)
        
print(revers1((input('Input your list:\n'))))

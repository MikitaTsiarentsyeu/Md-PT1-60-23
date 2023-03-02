WS = "Transmission"

a = input (f"{WS} - количество вхождений какого символа\n")
def Qwrap (WS, a, x=0):
   
    if len(WS) == 0:
        return x
    if WS[0] == a:
        x+=1
    
    return Qwrap(WS[1:], a, x) 

print(Qwrap(WS, a))
a = [2, 3, 8, 9]

def ranges(a):
    pointer1, pointer2= 0 ,0
     
    WS = ""
    lengh = len(a)

    while pointer2 < lengh:
        while pointer2 < lengh-1 and a[pointer2]+1 == a[pointer2+1]:
            pointer2 += 1

        WS += str(a[pointer1])
        if pointer1 != pointer2:
            WS += f"-{a[pointer2]}"

        if pointer2 < lengh-1:
            WS += ", "
            
        pointer1, pointer2 = pointer2 + 1, pointer2 + 1

       
    return WS

print(ranges(a))
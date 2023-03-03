a = [4,7,10]
# a = [2, 3, 8, 9]
# a = [0, 1, 2, 3, 4, 7, 8, 10]

def solution(list: a) -> str:
    n =  0 
    WS = str(a[0])
    for left_num, right_num in zip(a, a[1:]):
        
        if left_num+1 == right_num:
            if n>0:
                n =  0 
                WS = WS[:-(len(str(right_num))+1)]           
            WS+= f"-{right_num}"
            n += 1
                    
        else:
            WS+=f", {right_num}" 
            n=0

    return WS
print (solution(a))
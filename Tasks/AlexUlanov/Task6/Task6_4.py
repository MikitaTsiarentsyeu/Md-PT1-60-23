a  = int(input (" Число\n"))
b  = int(input (" Степень\n"))

def STEPEN(a, b, result = 1):
   
    if b == 0:
        return result
    if b > 0:

        result *= a
                
    return STEPEN(a, b-1, result)


print (STEPEN(a, b))
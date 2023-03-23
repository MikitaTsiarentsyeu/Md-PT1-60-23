b  = int(input ("Какую цифру по счету в последовательности ФИБО вывести\n"))


def Fibo(b, result=1, x=1, prevResult=1):

    if b == 1:
        return result
    prevResult = result
    result += x
    x = prevResult
    
    return Fibo(b-1, result, x, prevResult)

print(Fibo(b))
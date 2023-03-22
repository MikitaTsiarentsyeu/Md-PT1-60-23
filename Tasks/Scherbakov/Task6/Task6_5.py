n = int(input())

#def fibo(a):
#    if a == 0:
#        return 0
#    if a == 1:
#        return 1
#    else:
#        return fibo(a - 1) + fibo(a - 2)
def fibo(n):
    if n in (1, 2):
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(n))
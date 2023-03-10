s = int(input())
def fib_num(n):
    if n<=1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_num(n-1)+fib_num(n-2)
print(fib_num(s+1))
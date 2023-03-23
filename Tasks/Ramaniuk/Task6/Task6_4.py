x = int(input("Input your base number:\n"))
y = int(input("Input your exponent:\n"))
def power(n,m):
    if n==0 or n==1:
        return n
    else: 
        if m==1:
            return n
        elif n!=1:
            return n*power(n,m-1)
print(power(x,y))
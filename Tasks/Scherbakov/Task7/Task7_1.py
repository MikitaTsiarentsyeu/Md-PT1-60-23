n1 = int(input('Enter the numerator:\n'))
n2 = int(input('Enter the denominator:\n'))

def divizion(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        #if b == 0:
        return 'Cannot divide by zero'
   
print(divizion(n1,n2))

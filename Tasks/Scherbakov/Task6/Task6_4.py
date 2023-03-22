s = int(input('Enter the number you want to power:\n'))
s2 = int(input('Enter the power:\n'))

def power(a,b):
    if b <= 0:
        return 1
    else:
        return a * power(a,b - 1)
    
print(power(s,s2))
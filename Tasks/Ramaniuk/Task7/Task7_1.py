x=int(input("Input numerator:\n"))
y=int(input("Input denomerator:\n"))

def division(a,b):
    return a/b

try:
    print(division(x,y)) 
except ZeroDivisionError:
    print('Can not divide by zero')
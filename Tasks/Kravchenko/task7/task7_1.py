# 1. Write a function that takes two numbers as input 
# and returns their division. Handle the ZeroDivisionError 
# and return "Cannot divide by zero" if the denominator is zero.

a = int(input('Enter the first number\n'))
b = int(input('Enter the second number\n'))
def div (a: int, b: int):
    res = a/b
    return res    
        
try:
    print(div(a,b))
except ZeroDivisionError:
    print('Cannot divide by zero')


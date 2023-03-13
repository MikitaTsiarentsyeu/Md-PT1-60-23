'''Write a function that takes two numbers as input and returns their division.
Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.'''

def division_num(*args):
    a,b = int(input()), int(input())
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Cannot divide by zero')

division_num()
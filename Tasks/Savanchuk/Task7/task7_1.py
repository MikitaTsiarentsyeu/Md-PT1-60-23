#Write a function that takes two numbers as input and returns their division. Handle the ZeroDivisionError 
#and return "Cannot divide by zero" if the denominator is zero.
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero") 
print(division(a = int(input('Enter the first number:\n')),
                b = int(input('Enter the second number:\n'))))
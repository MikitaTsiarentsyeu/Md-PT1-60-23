def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except:
        return "Invalid data input"

print(divide(3,0))        
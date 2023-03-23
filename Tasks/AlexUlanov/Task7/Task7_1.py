x = int(input("Enter your fisrt number fo divide\n"))
y = int(input("Enter your second number fo divide(denominator)\n"))

def divide (x,y):
    try:
        return x/y
    except:
        print("Cannot divide by zero")
        return False
   

print (divide (x,y))
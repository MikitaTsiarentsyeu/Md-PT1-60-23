import time

x = int(input("Enter your fisrt number fo divide\n"))
y = int(input("Enter your second number fo divide(denominator)\n"))

def divide (x, y):
    try:
        return x/y
    except:
        print("Cannot divide by zero")
        return False

def log(func):
    def wrapper():
        start = time.time()
    
        z= func(x, y)
        with open ("log.csv", "a", encoding="utf-8") as f:           
            WS = "Time;X;Y;Z\n"
            f.write (WS)
            end = time.time()
            WS = str(end-start) + ";" + str(x) + ";"  + str(y) + ";"  + str(z) + "\n"  
            f.write (WS)
    return wrapper

loG = log(divide)
loG()


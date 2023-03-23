while True:
    a = input("Enter the first number:\n")
    b = input("Enter the second number:\n")
    if not a.isdigit() or not b.isdigit():
        print("Please use only numbers!")
        continue
    a, b = int(a), int(b)
    break    
def sumNum (a, b):
    return a + b
print(f"The sum of the numbers is {sumNum(a, b)}")     
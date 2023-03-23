x = input("Enter list of your numbers separated by space\n")

def EvenNums (x):
    x = x.split()
    y = 0
    
    try:
        if len(x) <= 1:
            raise ValueError("TWO or more digits needed")
        
        for i in range(len(x)):
            if int(x[i]) % 2 :
                pass
            else: 
                y += int(x[i])
    
    except ValueError as o:
        print(o)
        return False
           
    return y

print (EvenNums(x))
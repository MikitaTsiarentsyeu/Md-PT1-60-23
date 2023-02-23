a = input("Enter a list of strings:\n")
def countSymb (a):
    counterUpper = 0
    counterLower = 0
    for i in a:
        if i.isupper() :
            counterUpper += 1
        if i.islower():
            counterLower +=1 
    return counterUpper, counterLower        
print(f" Count of upper case symbols and count of lower case symbols: {countSymb(a)}")    
       

your_string = input("Input any string:\n")
def count_funk(string):
    u = 0
    l = 0
    for i in string:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    print(f"The number of upper case symbols: {u}, the number of lower case symbols: {l}")
    return u, l
count_funk(your_string)
   
       
    


name=input("Input name of your text file:\n")

try:
    with open(name,'r')as f:
        s = f.readlines() 
        for i in s: 
            print(i)
except FileNotFoundError:
    print("File not found")
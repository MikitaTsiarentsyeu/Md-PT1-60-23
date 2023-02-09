a = input("Please enter your digits (examle: 3 5 7 4)\n")
a=a.split()
b=0
for i in range (len(a)):
    b+=float(a[i])
b=b/(len(a))
    
print(round(b,2))
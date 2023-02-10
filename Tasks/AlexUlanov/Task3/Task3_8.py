#8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.

a = input("Please enter your digits (examle: 3 5 7 4)\n")
a=a.split()
b=0
for i in range (len(a)):
    b+=float(a[i])
b=b/(len(a))
    
print(round(b,2))
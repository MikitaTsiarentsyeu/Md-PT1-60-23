#10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.


def find_Largest(arr):
    Largest = c[0]
    Largest_index = 0
    for i in range(1, len(c)):
        if int(c[i]) > Largest:
            Largest = c[i]
            Largest_index = i
    return Largest_index 

a = input("Please enter your digits (examle: 3 5 7 4)\n")
a=a.split()
c=[]
for i in range (len(a)):
    b=int(a[i])
    if b % 2 > 0:
        if b % 3 > 0:          
            c.append(b)  
    if (b==2 or b ==3):
        c.append(b)  


print(f"Largest={c[find_Largest(c)]}")


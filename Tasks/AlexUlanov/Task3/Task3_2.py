#2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

def SummEven(a):
    a=a.split()
    summ = 0
    for i in range (len(a)):
        c = int(a[i])
        if c % 2==0:
            summ+=c

    return summ

a = input("Please enter your digits (examle: 3 5 7 4)\n")


print(SummEven(a))






# Write a program that takes a list of numbers as input and returns the average of all numbers in the list.

your_list = [int(i) for i in input('Enter numbers separated by spaces:\n').split()]

summ=0
n=0
for i in your_list:
    summ+=i
    n+=1
print(summ/n)
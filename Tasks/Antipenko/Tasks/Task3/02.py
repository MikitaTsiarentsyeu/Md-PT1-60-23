# Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

list_of_numbers = input('Enter numbers separated by spaces:\n').split()

sum = 0
for number in list_of_numbers:
    if int(number) % 2 == 0:
        sum += int(number)
print(sum)

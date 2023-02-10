# Write a program that takes a list of numbers as input and returns the largest prime number in the list.

your_list = [int(i) for i in input('Enter numbers separated by spaces:\n').split()]

largest_prime_number=0
for number in your_list:
    for i in range(2, number):
        if(number % i) == 0:
            break
    else:
        largest_prime_number=number
print(largest_prime_number)

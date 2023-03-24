def sum_of_even_numbers(l):
    count = 0
    for i in l:
        if i % 2 == 0:
            count += i
    return count
try:
    print(sum_of_even_numbers(input("Input any numbers separeted by commas:\n")))
except TypeError:
    print("Invalid input type")




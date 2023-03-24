def sum_of_even(numbers):
    res = 0
    for i in numbers:
        try:
            i == int(i)
        except ValueError:
            return "Invalid input type"
        if int(i) % 2 == 0:
           print(f'{res} + {int(i)} = {res+int(i)}')
           res = res + int(i)
    return print(f'The sum of all even numbers in the list: {res}')


sum_of_even(input("Enter a list of integers:\n"))
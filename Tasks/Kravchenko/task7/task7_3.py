# +3. Write a function that takes a list of integers as input 
# and returns the sum of all even numbers in the list. Handle 
# the TypeError and return "Invalid input type" if the input 
# is not a list or not every element is int.


def sum_even_nums(numbers_lst):
    try:
        if isinstance(numbers_lst, list):
            numbers_lst = [num for num in numbers_lst if num % 2 == 0]
            return sum(numbers_lst)
        else:
            raise TypeError
        
    except TypeError:
            return 'Invalid input type'

print(sum_even_nums([1, 5, 6, 'f']))
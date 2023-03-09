'''Write a function that takes a list of integers as input and returns the sum of all even numbers in the list.
Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.'''

k=[7,345,65,34,87,56,'345',782,[5,6,34],'erw',(89,11), {71:'71', 82:'82'}]
h=[2,4,8,18]

def summ(li):
    try:
        isinstance(li,list)
        summ = 0
        for i in li:
            isinstance(i,int)
            if i % 2 == 0:
                summ += i
        return summ
    except TypeError:
        return 'Invalid input type'



print(summ(k))
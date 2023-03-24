nth_number = int(input('Input index number of Fibonacci sequence\n'))

def Fibonacci(nth_number, n = 1, i = 1, j = 2):
    if n == nth_number:
        return i
    res = i+j
    return Fibonacci(nth_number,n+1, j, res)

print(f"The value of {nth_number}th number in Fibonacci sequence is {Fibonacci(nth_number)}")

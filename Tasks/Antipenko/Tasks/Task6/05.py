'''5. Write a recursive function to find the nth number in the Fibonacci sequence.
0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144'''


def fibo(x, y=0, z=1):
    if x == 1:
        return 0

    if x == 2:
        return 1

    return y + fibo(x - 1, z, y + z)


print(fibo(13))

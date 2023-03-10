def sum_even(x):
    sum=0
    if len(x)<=1:
        raise RuntimeError
    for i in x:
        if i%2==0:
            sum+=i
    return sum

try:
    print(sum_even(list(map(int, input("Enter your int numbers separeted by space:\n").split()))))
except TypeError:
    print("Invalid input type")
except ValueError:
    print("Try to enter only int numbers")
except RuntimeError:
    print("More than 2 numbers needed")
def sum_func(integer1, integer2):
    text = (f'The sum of {a} and {b} are {x}')
    print(text)

a, b = list(map(int,(input().split())))
x = a + b

sum_func(integer1=a, integer2=b)

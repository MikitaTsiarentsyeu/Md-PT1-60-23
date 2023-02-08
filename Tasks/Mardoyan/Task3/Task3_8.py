print('Hello!I can return the average of all numbers in your list.')
x = input('Input you list of numbers(Throught "space")\n')
count = 0
x = x.split(' ')
for i in x:
    count += int(i)
print(round(count / len(x), 2))
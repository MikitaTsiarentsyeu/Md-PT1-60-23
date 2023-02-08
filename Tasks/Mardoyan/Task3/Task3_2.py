print('Hello!I can help you count the even numbers on your list')
x = input('Input you list of numbers(Throught "space")\n')
count = 0
x = x.split(' ')
for i in x:
    if int(i) % 2 == 0:
        count +=1
print(count, 'of even numbers')
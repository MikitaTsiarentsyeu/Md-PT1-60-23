print('Hello!I can return the secpnd largest number on your list of numbers.')
x = input('Input you list of positive numbers(Throught "space")\n')
x = x.split(' ')
larg_n1 = 0
larg_n2 = 0
for i in x:
    if int(i) > larg_n1:
        larg_n1 = int(i)
for i in x:
    if int(i) > larg_n2 and int(i) != larg_n1:
        larg_n2 = int(i)
print(larg_n2)
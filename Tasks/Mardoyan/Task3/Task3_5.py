print('Hello!I can return a list with all strings that have a length greater than 5 characters.')
x = input('Input you list of strings(Throught "space")\n')
x = x.split(' ')
count = []
for i in x:
    if len(i) > 5:
        count.append(i)
if not count:
    print('All strings are less than 5 characters')
else:
    print(count)
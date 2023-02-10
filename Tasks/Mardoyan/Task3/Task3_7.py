print('Hello!I can return string with all capital letters converted to lowercase and vice versa.')
x = input('Input you string(on English)\n')
d = ''
for i in x:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
       d += i.lower()
    elif i in 'qwertyuiopasdfghjklzxcvbnm':
       d += i.upper()
    elif i in ' ':
       d += i 
print(d)
print('Hello!I can return the string reversed.')
x = input('Input you string(on English)\n')
d = ''
for i in x[::-1]:
    d += i 
print(d)
l = input('enter a string\n')

for i in l:
    if i.istitle():
        print(i.lower(), end='')
    else: 
        print(i.upper(), end='')
print()
l = input('enter a list of numbers separated by a space\n')
l = l.split()

s = 0
for i in l:
    i = int(i)
    if i % 2 == 0:
        s = s + i 
print(s)
l = input('enter a list of numbers separated by a space\n')
l = l.split()
s = 0

for i in l:
    i = float(i)
    s += i

s = s/2
print(s)

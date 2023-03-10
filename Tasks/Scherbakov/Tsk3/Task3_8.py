n = input('Enter your numbers wiht a "space":\n').split()

h = 0

for i in n:
    h += int(i)
    
print(h/len(n))

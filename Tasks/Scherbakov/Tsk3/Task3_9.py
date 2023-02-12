st = input('Enter your numbers wiht a "space":\n').split()

n = 0

sm = 0

for i in st:
    sm += int(i)
    n += 1
 
print('Average of all numbers in the list is equal to:' + str(round(sm/n)))
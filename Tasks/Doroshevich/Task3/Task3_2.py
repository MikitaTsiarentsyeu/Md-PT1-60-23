import random
l = [random.randint(-10, 10) for i in range(10)]

print(l)

summ = 0

for x in l:
    if not x % 2:
        summ += x
        
print (summ)
import random
mas = []
sum = 0
mas = [random.randint(1,100) for i in range(1,18)]
print(mas)
for i in mas: 
    if (i%2) == 0:
        sum += i

print(sum)
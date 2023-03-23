import random
# List of numbers generator
l = [random.randint(-100, 100) for i in range(10)]
print(l)

summ, amount = 0, 0
for i in l:
    summ += i
    amount += 1
print(summ / amount)
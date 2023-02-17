S = input("Input your space-separated numbers:\n").split()
sum = 0
x = 0
for i in S:
    sum = sum + int(i)
    x += 1
average = sum / x
print(average)
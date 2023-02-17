n = int(input('Enter the five numders:\n'))

x = [int(a) for a in str(n)]

b = 0

for i in range(1, len(x)):
    if x[i] > x[b]:
        b = i

print(x, x[b - 1])

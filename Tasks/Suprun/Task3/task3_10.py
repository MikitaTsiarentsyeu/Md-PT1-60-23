print("I can find the largest prime number in the number range you specified")
f = int(input("Enter the first number of the range:\n"))
s = int(input("Enter the last number of the range:\n"))
l = []
for i in range(f, s):
    d = 2
    while i % d != 0:
        d += 1
    if d == i:
        l.append(i)
m = 0
for i in range(1, len(l)):
    if l[i] > l[m]:
        m = i
print(l[m])



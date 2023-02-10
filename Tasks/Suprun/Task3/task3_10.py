n = input("Let's find the largest prime number!\nEnter any numbers(separated by commas)\n")
n = list(n.split(','))
lst = []
m = 0
for i in n:
    if (int(i) % 2 != 0 or int(i) == 2) and (int(i) % 3 != 0 or int(i) == 3) and (int(i) % 5 != 0 or int(i) == 5):
        lst.append(i)
for i in lst:
    if int(i) > m:
        m = i
print(m)
    

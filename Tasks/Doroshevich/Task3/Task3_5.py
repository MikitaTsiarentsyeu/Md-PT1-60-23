import random
import string

#  list of strings generator
l = []

for i in range(0, 10):
    l_string = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))
    l.append(l_string)

print(l)

# Solution
l1 = []

for i in l:
    n = 0
    for j in i:
         n += 1
         if n > 5:
            l1.append(i)
            break

print(l1)
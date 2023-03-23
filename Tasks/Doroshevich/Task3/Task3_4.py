import random
# List of numbers generator
l = [random.randint(-100, 100) for i in range(random.randint(2, 20))]
print(l)
l = list(set(l))
if len(l) == 1:
    print("All elements of the list are equal. Try again")
    exit()

# 1st way
m = 0
for i in range(1, len(l)):
    if l[i] > l[m]:
        m = i
m_num = l[m]

m = 0
for i in range(1, len(l)):
    if l[i] > l[m] and l[i] != m_num:
        m = i
print(l[m])

# 2nd way
#  I think this method to be a priority because using this solution
#  you can find any n-th element from the list by changing only 1 digit in the code
m = 0
j = 0
while j < 2:
    for i in range(1, len(l)):
        if l[i] > l[m]:
            m = i
    j += 1
    if j < 2:
        l.remove(l[m])
        m = 0

print(l[m])

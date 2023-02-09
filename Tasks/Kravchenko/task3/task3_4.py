n = input().split()
s = set()
# set in order to ignore duplicates
for i in n:
    i = int(i)
    s.add(i)

m1 = float('-inf')
m2 = float('-inf')


for val in s:
    if m1 <= val:
        m2 = m1
        m1 = val
    elif m2 <= val:
        m2 = val
       

print(m2)

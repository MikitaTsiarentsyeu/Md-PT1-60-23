l = (input('enter a list of numbers separated by a space\n')).split()
new_l = []

for i in l:
    i = int(i)
    if i==2 or i==3:
        new_l.append(i)
    if i%2==0 or i%3==0 or i==1:
        continue
    new_l.append(i)

m = 0

for i in range(1,len(new_l)):
    if new_l[i] > new_l[m]:
        m = i

print(new_l[m])

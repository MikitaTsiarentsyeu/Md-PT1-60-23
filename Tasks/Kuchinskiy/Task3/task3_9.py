user = input('enter world\n')
new_s = []

for i in user:
    new_s.insert(0,i)

print(''.join(new_s))
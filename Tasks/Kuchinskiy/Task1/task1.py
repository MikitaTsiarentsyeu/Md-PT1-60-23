dep = int(input('Enter deposit amount:\n'))
date = int(input('Enter the retention period in months:\n'))
per = int(input('Enter annual percentage:\n'))
per = per/12

for i in range(date):
    s = (dep * per)/100
    dep = dep + s

print(f'Account amount: {round(dep, 2)} BYN')
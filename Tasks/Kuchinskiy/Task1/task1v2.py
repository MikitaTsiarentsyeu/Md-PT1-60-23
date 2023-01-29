def test(x):
    while x.isdigit()==False:
        x = input("You didn't enter a number. Try again:\n")
    return x

x = test(input('Enter deposit amount:\n'))
dep = int(x)

x = test(input('Enter the retention period in months:\n'))
date = int(x)

x = test(input('Enter annual percentage:\n'))
per = int(x)
per = per/12

for i in range(date):
    s = (dep * per)/100
    dep = dep + s

print(f'Account amount: {round(dep, 2)} BYN')
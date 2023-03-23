
string=int(input("Enter the number and I'll show you some magic:\n "))

for i in range(2,string):
    k = 0
    for j in range(2,i-1):
        if i % j== 0:
            k=k+1
    if k == 0:
        print(f'All prime numbers before your number is: {i}')
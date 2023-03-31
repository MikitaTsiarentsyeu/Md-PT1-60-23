user_numb = input("Please, type any numbers in format 'a b c d e f':\n").split()
                                  # 12 13 17 16 55 87 41 2 31 3 6 53 97 58 4 122 99 54 58 51 103 113 83 73 67
numbers = []
prime_numb = []

for e in user_numb:
    if e.isdigit():
        numbers.append(int(e))

for num in numbers:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numb.append(num)

prime_numb.sort()

print(prime_numb)
print("The largest prime value is", prime_numb[-1])


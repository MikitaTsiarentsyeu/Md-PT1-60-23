numbers = [1, 4, 6, 2, 47, 25, 44, 22, 67, 84, 33, 74]

prime_num = []

for number in numbers:
    for i in range(2, number):
        if number % i == 0:
            break
else:
    prime_num.append(number)
max_prime_num = max(prime_num)

print(f" The largest prim number in the list is:{max_prime_num}")

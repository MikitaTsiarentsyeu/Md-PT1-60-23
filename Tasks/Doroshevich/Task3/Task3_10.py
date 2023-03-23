import random
# List of numbers generator
l = [random.randint(2, 102) for i in range(20)]

l_prime = []

for j in l:
    i = 2
    while i <= j**.5:
        if not j % i:
            break
        i += 1
    else:
        l_prime.append(j)

m = 0
n = 0

for i in l_prime:
    n += 1

for i in range(1, n):
    if l_prime[i] >= l_prime[m]:
        m = i

print("", l, "- list of numbers\n", l_prime, "- list of primes numbers\n", l_prime[m], "- max prime number")

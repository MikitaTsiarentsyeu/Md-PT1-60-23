import math
def is_prime(t):

    for i in range(2, int(math.sqrt(t)) + 1):
        if t % i == 0:
            return False
        
    return True
print("Введите список:")

maxim = 0
number = list(map(int, input().split()))

for i in number:
    if is_prime(i) and i > maxim and i != 1:
        maxim = i

if (maxim == 0):
    print("Простых чисел в вашем списке нет")
else:
    print("Максимальное простое число в вашем списке:", maxim)

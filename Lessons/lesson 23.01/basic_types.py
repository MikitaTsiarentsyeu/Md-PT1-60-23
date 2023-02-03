x = 5555
print(type(x))

print(12*3)
print(12+3)
print(12-3)
print(12//3)

print(int(2.8))
print(int(-2.8))

# print(int("two"))

print(type(8.8//2.2))
print(12.0//3.5)
print(round(3.5), round(4.5), round(5.5), round(6.5), round(7.5))

print(1.1+1.1+1.1)

import decimal
d = decimal.Decimal('1.1')
print(d+d+d)

import fractions
f = fractions.Fraction('2.4')
print(f)

import math
print(math.sqrt(144))
print(math.cos(math.pi))
print(type(math.inf))

import random
print(random.randint(10, 20))
l = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(l)
print(l)
print(random.choice(l))
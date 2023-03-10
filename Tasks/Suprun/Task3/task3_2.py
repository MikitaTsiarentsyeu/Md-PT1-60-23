s = input ("I can count the sum of all even numbers. Enter any numbers(separated by commas):\n")
s = list(s.split(','))
sum = 0
for  i in s:
    i = int(i)
    if i % 2 == 0:
        sum += i
print(sum)
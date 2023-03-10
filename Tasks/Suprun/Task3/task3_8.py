s = input ("Let's count the average of numbers!\nEnter any numbers(separated by commas):\n")
s = list(s.split(','))
aver = 0
for i in s:
    i = int(i)
    aver = aver + i
print(aver//len(s))
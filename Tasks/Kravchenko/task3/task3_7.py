s = input()
a_lower = 'abcdefghijklmnoprqstuvwxyz'
a_upper = 'ABCDEFGHIJKLMNOPRQSTUVWXYZ'
for i in s:
    if i in a_lower:
        s_ = a_upper[a_lower.find(i)]    
    elif i in a_upper:
        s_ = a_lower[a_upper.find(i)]
    print(s_, end = '')
print()


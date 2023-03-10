def count_s(s):
    low_letter = 0
    cap_letter = 0
    for i in range(len(s)):
        if s[i].islower():
            low_letter += 1
        elif s[i].isupper():
            cap_letter += 1
    return(f'low:{low_letter},cap:{cap_letter}')

print(count_s('My First Program'))
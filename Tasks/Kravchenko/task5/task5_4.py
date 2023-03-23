s = input()

def lower_upper_case(s):
    n_lower = 0
    n_upper = 0
    for i in s:
        if i.isalpha() and i.islower():
            n_lower += 1
        elif i.isalpha() and i.isupper():
            n_upper += 1
        else:
            continue
    return n_lower, n_upper
print(lower_upper_case(s))



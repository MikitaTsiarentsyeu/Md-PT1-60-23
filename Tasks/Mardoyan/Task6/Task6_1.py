def rev_func(s):
    if len(s) == 1:
        return s
    return rev_func(s[1:]) + s[0]

x = input('Input string\n')
print(rev_func(x))
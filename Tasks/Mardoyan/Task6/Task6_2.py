def pall_func(s):
    if len(s) < 1:
        return True
    elif s[0] == s[-1]:
        return pall_func(s[1:-1])
    else:
        return False

x = input('Input string\n')
print(pall_func(x))
    
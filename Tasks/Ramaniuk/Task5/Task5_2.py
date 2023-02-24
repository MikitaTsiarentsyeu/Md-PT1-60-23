def rev_string(x):
    res = ''
    for i in x[::-1]:
        res += i[::-1]
        res += ' '
    return res
print(rev_string(input("Write your text:\n").split()))
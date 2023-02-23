def num_let(x):
    l = 0
    u = 0
    res = ''
    for i in x:
        if i.isupper():
            u += 1
        else:
            l += 1
    res = l, u
    return res
print(num_let(input("Put your string:\n")))
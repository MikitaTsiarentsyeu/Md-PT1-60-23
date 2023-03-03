def revers_funk(arg, i = -1, rev_string=[]):
    if i == -(len(arg)+1):
        return
    else:
        rev_string.append(arg[i])
        revers_funk (arg,(i  -1))
    return "".join(rev_string)


rev_string = revers_funk('Какая-то строка')

print(rev_string)
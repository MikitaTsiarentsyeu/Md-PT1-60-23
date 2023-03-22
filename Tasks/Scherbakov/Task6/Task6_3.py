st = 'inputtt'
s1 = 'i'

def tocount (str, num, c = 0):

    if str[0] == num:
        c += 1

    if len(str) == 1:
        return c

    return tocount (str[1:len(str)], num, c)

print(tocount(st, s1))
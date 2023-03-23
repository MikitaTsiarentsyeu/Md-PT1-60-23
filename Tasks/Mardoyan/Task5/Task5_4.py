list = str(input('Input a string\n'))
lower = 0
upper = 0
def low_func(a):
    global lower
    for i in a:
        if i in 'qwertyuiopasdfghjklzxvbnm':
            lower += 1
    return lower
def upp_func(a):
    global upper
    for i in a:
        if i in 'QWERTYUIOPASDFGHJKLZXVBNM':
            upper += 1
    return upper
print('Count of lower case symbols -',low_func(list))
print('Count of upper case symbols -',upp_func(list))


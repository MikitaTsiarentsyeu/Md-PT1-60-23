strg = input('Enter your strings:\n').split()

def reverse_str(a):
    lst = []
    for i in range(len(a)):
        res = ''.join(reversed(a[i]))
        lst.append(res)
        i += 1
    return lst
        

print(reverse_str(strg))
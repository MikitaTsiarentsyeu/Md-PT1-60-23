s = input('Enter the string:\n')

def reverse(a):
    if a == "":
        return a
    else:
        return reverse(a[1:]) + a[0]
print(reverse(s))

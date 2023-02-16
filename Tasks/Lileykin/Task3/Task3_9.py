""" x="on the contrary"
x[::-1]
print(x) """

def reversed4(variable):
    res=''.join(reversed(variable))
    return res

n = reversed4(input())
print(n)
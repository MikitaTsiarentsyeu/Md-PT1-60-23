a = input("Enter a list of strings:\n")
def strRevers (a):
    return [i for i in a.split() if len(i) > 5]
print(strRevers(a))


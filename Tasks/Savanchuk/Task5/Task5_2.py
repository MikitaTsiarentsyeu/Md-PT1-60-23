a = input("Enter a list of strings:\n")
def strRevers (a):
    return [str(i[::-1]) for i in a] 
print(strRevers(a))
strg = input('Enter your strings:\n').split()

def five_symblols(a):
    lst= []
    a = [lst.append(a[i]) for i in range(len(a)) if len(a[i]) > 5] 
    return lst

print(five_symblols(strg))

a = input("Полидром?\n")
def palidrome(a):
    if len(a) % 2 == False:
        return False
    if len(a) == 1:
        return True
    if a[0] == a[-1]:
        palidrome(a[1:-1])
        return True
    else: 
        return False

    
print(palidrome(a))
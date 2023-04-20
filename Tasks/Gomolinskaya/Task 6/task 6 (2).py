def ispalindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return ispalindrome(s[1:-1])
        else:
            return False
a = str(input("Введите строку:"))
if (ispalindrome(a) == True):
    print("Палиндром")
else:
    print("Не палиндром")



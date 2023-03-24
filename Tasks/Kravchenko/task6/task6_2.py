s = input()
def palindrome(s):
    if len(s) == 1 or len(s) == 0:
        return "it is palindrome"
   
        
    i, j = 0, -1
    if s[i] == s[j]:
        return palindrome(s[1:-1])
    else:
        return "it's not palindrome"

    
    
print(palindrome(s))    
    

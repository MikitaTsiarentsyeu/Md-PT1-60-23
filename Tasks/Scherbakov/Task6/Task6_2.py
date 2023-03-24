s = input()

def palindrom(a):
    def reverse(a):
        if a == "":
            return a
        else:
            return reverse(a[1:]) + a[0]
    if reverse(a) == a:
        return 'This string is a palindrome'
    else:
        return 'This string is not a palindrome'
    
#def palindrom(a):
#    if a <= 1:
#        return 'This string is a palindrome'
#    if a[0] == a[-1]:
#        return 'This string is a palindrome'
#    else:
#        #return palindrom(a[1:-1])
  
print(palindrom(s))
'''2. Write a recursive function to check whether a given string is a palindrome.'''

def is_palindrome(st):
    if len(st) < 1:
        return True
    else:
        if st[0] == st[-1]:
            return is_palindrome(st[1:-1])
        else:
            return False
sent = str(input("Enter the string:\n"))
if (is_palindrome(sent) == True):
    print("This string is a palindrome")
else:
    print("This string is not a palindrome!")
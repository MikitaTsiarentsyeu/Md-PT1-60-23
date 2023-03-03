def palindrime_string(palindrome):
    palindrome = str(palindrome).replace(' ', '')
    if len(palindrome) <= 1:
        print("it's a palindrome")
        return
    else:
        return palindrome[0] == palindrome[-1] and palindrime_string(palindrome[1:-1])
palindrime_string(input())


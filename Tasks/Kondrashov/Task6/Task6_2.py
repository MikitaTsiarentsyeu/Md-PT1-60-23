def palindrome(text):
    if len(text) < 1:
        return 'перевертыш'
    else:
        if text[0] == text[-1]:
            return palindrome(text[1:-1].strip())
        else:
            return "Не палиндром !"

print(palindrome(text=input("")))
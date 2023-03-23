def is_palindrome(n):
    if len(n) < 1:
        return True
    else:
        if n[0] == n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False
word=str(input("Введите произвольное слово:\n"))
if(is_palindrome(word)==True):
    print("Полидромно")
else:
    print("Не полидромно")
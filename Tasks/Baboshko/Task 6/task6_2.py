def palindrome(s):
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return True + palindrome(s[1:-1])
        else:
            return False
letter = ''.join(input('Введите вашу строку для проверки:\n').split())
if palindrome(letter) == len(letter)/2 + 1:
    print('Да')
else:
    print('Нет')

#1 reverse a string
def rev_str(str):
    return str if str == '' else rev_str(str[1:]) + str[:1]

print(rev_str('string'))


#2 string is a palindrome
def pal_str(str):
    if len(str) < 1: return True
    if str[0] == str[-1]:
        return pal_str(str[1:-1])
    else: return False
    
print(pal_str('madam'))


#3 occurrences character
def occur_char(str, char):
    return 0 if not str else occur_char(char, str[1:]) + 1

print(occur_char('striiing', 'i'))


#4 power
def power(num, exp):
    if (exp == 1): return (num)
    if (exp != 1):
        return (num * power(num, exp - 1))

print(power(2, 5))


#5 Fibonacci
def fib(n):
    if n in (0, 1): return 1 
    else:
        f_1, f_2 = n - 1, n - 2
        return fib(f_1) + fib(f_2)
    
print(fib(7))

    

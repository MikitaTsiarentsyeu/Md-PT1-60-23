import random


def reverse(s):

    if len(s) == 1:
        return s

    return s[-1] + reverse(s[:-1])


print(reverse("qwerty"))


def palindrome_check(s):

    s = ''.join(s.split())

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome_check(s[1:-1])


print(palindrome_check("qwerty trewq"))


def counter_of_occurrences(s, symbol, counter=0):

    if s == '':
        return 0

    if s[0] == symbol:
        counter += 1

    return counter + counter_of_occurrences(s[1:], symbol)


print(counter_of_occurrences('ssaddsaddddgt', 'd'))


def power_of_number(number, power):

    if power == 1 or number in range(2):
        return number

    return number * power_of_number(number, power - 1)


print(power_of_number(2, 10))


def fibonacci(n, a=0, b=1):

    if n == 1:
        return 0

    if n == 2:
        return 1

    return a + fibonacci(n-1, b, a+b)


print(fibonacci(10))

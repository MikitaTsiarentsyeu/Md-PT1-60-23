import random


def reverse(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse(s[:-1])


print(reverse("qwerty"))


def palindrome_check(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome_check(s[1:-1])


print(palindrome_check("qwertytrewq"))


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


def merge_sort(l):
    if len(l) == 1:
        return l
    return compare_rec(merge_sort(l[:len(l)//2]), merge_sort(l[len(l)//2:]))


def compare_rec(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    return [l1[0]] + compare_rec(l1[1:], l2) if l1[0] <= l2[0] else [l2[0]] + compare_rec(l1, l2[1:])


def random_list(length, l=[]):
    if len(l) == length:
        return l
    return [random.randint(0, 50)] + random_list(length-1, l[:length - 1])


random_list = random_list(16)
print(random_list, '\n', merge_sort(random_list))

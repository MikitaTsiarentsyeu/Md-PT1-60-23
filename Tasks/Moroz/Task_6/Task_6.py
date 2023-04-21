# 1. Write a recursive function to reverse a string.

my_str = "hello aliens"

def str_reverse(my_str):
    if not my_str:
        return my_str

    temp = my_str[0]
    str_reverse(my_str[1:])
    print(temp, end="")

print(str_reverse(my_str))


# 2. Write a recursive function to check whether a given string is a palindrome.

strng = "ATA"

def palindrome_checker(strng: str) -> str:
    if len(strng) <= 1:
        return "a palindrome"
    if strng[0] == strng[len(strng)-1]:
        palindrome_checker(strng[1:len(strng)-1])
        return "a palindrome"
    else:
        return "not a palindrome"

print(palindrome_checker(strng))


# 3. Write a recursive function to count the number of occurrences of a given character in a string.

strng="aaa"
char="a"
def num_of_occurrences(strng: str, char: str, coun=0) -> int:
    if not strng:
        return coun
    elif strng.index(char):
        return num_of_occurrences(strng[strng.index(char)+1:], char, coun+1)
    else:
        return num_of_occurrences(strng[strng.index(char)+1:], char, coun+1)


print(num_of_occurrences(strng, char, coun=0))


# 4. Write a recursive function to calculate the power of a given number.

def power(num1, num2):
    if num2 != 0:
        return num1 * power(num1, num2 - 1)
    else:
        return 1

print(power(2,2))


# 5. Write a recursive function to find the nth number in the Fibonacci sequence.
# 0, 1, 2, 3, 5, 8, 13, 21

def fibon(n):
    if n < 2:
        return n
    else:
        return fibon(n - 1) + fibon(n - 2)

print(fibon(8))
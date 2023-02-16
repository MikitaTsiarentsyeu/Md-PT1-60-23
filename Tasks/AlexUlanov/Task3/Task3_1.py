#1. Write a program that takes a string as input from a user and returns the number of vowels in the string.

def qualityVovels(a):
    Dict1 = ["a", "e", "i", "o", "q", "y", "u"]
    b = 0
    for i in range (len(a)):
        if (a[i] in Dict1):
            b+=1

    return b


a = input("Please enter your question")


print(qualityVovels(a))

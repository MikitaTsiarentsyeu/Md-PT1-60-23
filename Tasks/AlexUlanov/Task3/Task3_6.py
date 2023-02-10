#6. Write a program that takes a string as input and returns the string with all vowels removed.

a = "Please enter your question"
Dict1 = ["a", "e", "i", "o", "q", "y", "u"]
b=""
for i in range (len(a)-1):
    if a[i] in Dict1:
        b+=" "
        continue
    b+=a[i]
    

print(b)

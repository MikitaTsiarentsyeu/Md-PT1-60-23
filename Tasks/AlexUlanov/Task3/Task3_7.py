#7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.

a = input("Please enter your question")

b=""
for i in range (len(a)):
    if a[i].istitle():
        b+=a[i].lower()
    else:
        b+=a[i].upper()
    
print(b)

a = input("Please enter your question")

b=""
for i in range (len(a)):
    if a[i].istitle():
        b+=a[i].lower()
    else:
        b+=a[i].upper()
    
print(b)

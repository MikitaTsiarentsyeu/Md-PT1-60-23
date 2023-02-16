message=input("Enter text\n")

for i in range(len(message)):   
    if message.isupper():
        if message[i].upper():
            x=message.lower()
        print(x)
        quit()
    else:
        print(message.upper())
        quit()
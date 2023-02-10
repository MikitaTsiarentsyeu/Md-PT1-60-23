string  = input("I can count the number of vowels in your string.\nEnter any string:\n")
vowels = ['a','e','i','o','u']
n = 0
for elem in string:
    if elem in vowels:
        n += 1
print(n)    
    
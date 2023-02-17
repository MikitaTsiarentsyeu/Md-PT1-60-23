string = input("Enter any string:\n")
a = 0

for i in string.lower():
    if i in {'a','e','i','o','u','y'}:
        a += 1
        
print ("the number of vowels in your string:", a)
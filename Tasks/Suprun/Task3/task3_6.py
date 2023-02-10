string  = input("I'll remove all vowels!\nEnter any string:\n")
vowels = ['a','e','i','o','u']
for elem in vowels:
    string = string.replace(elem, '') 
print(string)
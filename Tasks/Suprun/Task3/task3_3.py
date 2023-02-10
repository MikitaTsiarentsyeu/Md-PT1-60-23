string = input ("Enter any string:\n")
string = string.split(' ')
d = {}
for elem in string:
    d[elem] = len(elem)
print(d)
    

    

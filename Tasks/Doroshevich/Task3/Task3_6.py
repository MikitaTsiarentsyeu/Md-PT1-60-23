string = input("Enter any string:\n")

#1st way
string1 = string
for i in string.lower():
        if i in {'a', 'e', 'i', 'o', 'u', 'y'} and i in string1:
            string1 = string1.replace(i, '')
            string1 = string1.replace(i.upper(), '')

#2nd way
l = list(string)
for i in l:
    if i in {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}:
        l.remove(i)
string2 = ''.join(l)

print(string1, '\n', string2)

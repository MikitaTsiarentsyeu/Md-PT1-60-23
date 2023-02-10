string = input("Enter any string:\n")
#1st way
s = ''
for i in string:
    s = f"{i}{s}"
print (s)

#2nd way
j = 0
l = []
for i in string:
    j += 1
while j > 0:
    l += string[j-1]
    j -= 1
s = ''.join(l)
print(s)
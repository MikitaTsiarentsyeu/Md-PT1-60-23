string = input("Enter any string:\n")
#1st way
l = list(string)
l1 = []
for i in l:
    i = i.upper() if i.islower() else i.lower()
    l1 += i
f_string = ''.join(l1)
print(f_string)

#2nd way 
# I think that this method is less preferable,
# because in it we create a new string with each iteration
s_swap = ''
for i in string:
    i = i.upper() if i.islower() else i.lower()
    s_swap += i
print(s_swap)

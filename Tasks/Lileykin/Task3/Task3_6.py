
string = input("input something\n")
vowels=('a', 'e', 'i', 'o', 'u', 'y')

string=string.lower()

for i in vowels:
    string=string.replace(i,'')

string='.'.join(string)
string=string.rjust(len(string)+1,'.')

print(string)
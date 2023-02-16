s = "test string data\n\n"

print(type(s), type(s[0]), type(s[2:5]))

print(len(s))

print(' ' in s)
print('str' in s)
print('utyfiu' in s)

print("new "+"string")
print(8*"test")

print("TeSt StRiNg".upper())
print("TeSt StRiNg".lower())
print("TeSt StRiNg".capitalize())

print(s.find(' '))
print(s.find('str'))
print(s.find('8r6y'))

print(s.replace(' ', '_'), s)
print(s.replace(' ', '_').replace('\n', '').replace('t', 'T'))

print("!!!te!!!!!!st!!!!!!!!".strip('!'))
print("!!!te!!!!!!st!!!!!!!!".replace('!', ''))

print(s.split())
print('_|_|_|'.join(s.split()))

s = "76353758:adidas_superstar63583bk"
print(s.split(':')[1].split("_"))


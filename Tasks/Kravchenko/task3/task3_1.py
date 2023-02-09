text = input()
s = 0
vowels = 'aeiou'
text = text.lower()
for i in text:
    if i in vowels:
        s += 1
print(s)


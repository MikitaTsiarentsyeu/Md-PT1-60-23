t = input()
t = t.lower()
vowels = 'aeiou'
l = []
for i in t:
    if i not in vowels:
        l.append(i)
print(*l, sep = '')
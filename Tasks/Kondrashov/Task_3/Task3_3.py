a = input('Enter something:\n')
b = {}
for i in a:
    b = a.split()
print(f'You wrote {len(b)} words,These words are: {b}')
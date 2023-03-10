st = input('Enter the sentence:\n').split()

list = []

for i in st:
    if len(i) > 5:
        list.append(i)

print(list)

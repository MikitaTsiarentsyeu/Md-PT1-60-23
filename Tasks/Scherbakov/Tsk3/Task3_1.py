s = input("Type any string\n:")

g = set("AaEeUuIiOoYy")

count = 0

for l in s:
    if l in g:
        count += 1
print("The number of vowels is equal to\n:")
print(count)


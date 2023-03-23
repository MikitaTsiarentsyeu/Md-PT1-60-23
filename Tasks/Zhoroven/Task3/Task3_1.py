x = input(" Enter any word:\n")
x = list(x)
print(x)

vowels_list = ['a', 'e', 'i', 'o', 'u']
total = 0

for i in x:
    if i in vowels_list:
        total += 1

if total == 1:
    print(f"{total} lowel")
else:
    print(f"{total} lowes")

string = input("Input your word(s), sentence or text:\n")
v = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
x = 0
for i in string:
    if i in v:
        x += 1
print(x)
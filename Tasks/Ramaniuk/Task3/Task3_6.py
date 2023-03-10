string = input("Input your word(s), sentence or text:\n")
v = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "Y", "y"]
for i in string:
    if i in v:
        string = string.replace(i, "")
print(string)
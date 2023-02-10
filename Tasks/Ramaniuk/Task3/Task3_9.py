string = input("Input your word(s), sentence or text:\n")
x = len(string)
s = []
while x > 0:
    s += string[x - 1]
    x = x - 1
print("".join(s))
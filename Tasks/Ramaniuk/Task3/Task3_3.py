string = input("Input your space-separated words, sentence or text :\n")
S = string.replace(",", " ")
S = string.replace("\n", " ")
S = string.replace(";", " ")
S = string.replace("?", " ")
S = string.replace("!", " ")
S = string.replace(":", " ")
S = string.split(" ")
d = {}
for i in range(1, len(S)+1):
    d[i] = S[i-1]
print(d)
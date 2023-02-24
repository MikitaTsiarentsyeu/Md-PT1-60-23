def string(x):
    res = ''
    for i in x:
        if len(i) > 5:
            res += i
            res += "."
    return res
print(string(input("Write your text:\n").split(".")))
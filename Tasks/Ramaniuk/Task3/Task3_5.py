l = input("Please, input your strings separeted by dot:\n").split(".")
for i in l:
    if len(i) <= 5:
        l.remove(i)
print(l)
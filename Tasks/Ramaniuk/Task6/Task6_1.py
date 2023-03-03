def revers(n):
    if len(n)==0:
        return n
    else:
        return revers(n[1:])+n[0]
print(revers(str(input("Write your text:\n"))))
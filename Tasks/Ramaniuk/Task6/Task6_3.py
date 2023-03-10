s = str(input("Write your symbol:\n"))
x = str(input("Write your text:\n"))
count = 0
def counter(n,m):
    if len(m)>=1:
        if n == m[0]:
            global count
            count += 1
            counter(n,m[1:])
        else:
            counter(n,m[1:])
    return count
counter(s,x)
print(count)
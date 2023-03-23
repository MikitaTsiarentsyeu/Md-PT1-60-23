a = []
c=""

b = int(input("Введите количество строк\n"))

for i in range(b):
    с = input(f"Введите {i+1} строчку\n")
    a.insert(i, с)


def more5 (n1):
    a1 = []
    n = 0
    for i in range(len(n1)):
        if len(n1[i])>5:
            c = n1[i]               
            a1.insert(n, c)
            n+=1   

    return a1

print(more5(a))
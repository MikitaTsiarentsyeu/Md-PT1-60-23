a = []
c=""

b = int(input("Введите количество строк\n"))

for i in range(b):
    с = input(f"Введите {i+1} строчку\n")
    a.insert(i, с)


def reflection (n1):
    a1 = []
    c1 = ""
    for i in range(len(n1)):
        c = n1[i]
        c1= c[::-1]
        a1.insert(i, c1)

    return a1

print(reflection(a))



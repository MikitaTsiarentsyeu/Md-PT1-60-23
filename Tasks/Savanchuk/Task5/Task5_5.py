a = input("Enter numbers separated by spaces:\n")   
a = {int(i) for i in a.split()} #убираю дубликаты, сортирую по возрастанию
a = list(a)
def getRanges (a):
    res = str(a[0])
    for i in range(len(a)-1):
        if a[i] + 1 == a[i+1]:
            if res[-1] != "-":
                res += "-"
            else:
                pass
        elif a[i] + 1 != a[i+1]:
            if f"{a[i]}" not in res:
                res += f"{a[i]}, {a[i+1]}"
            else:
                res += f", {a[i+1]}"
    if res[-1] == "-":
        res += f"{a[-1]}"
    return (res) 
print(getRanges(a))

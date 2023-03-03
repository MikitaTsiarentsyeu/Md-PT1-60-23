s = input("Write your text:\n").split(",")
s = list(s)

def list_num(x):
    num = ""
    n = 0
    for i in x:
        if int(i) == (int(x[n-1]) + 1):
            if n + 1 < len(x):
                if int(i) == (int(x[n+1]) - 1):
                    n += 1
                else:
                    num += i
                    num += ","
                    n += 1
            else:
                num += i
        else:
            num += i
            if n + 1 < len(x):
                if int(i) == (int(x[n+1]) - 1):
                    num += "-"
                    n += 1
                else:
                    num += ","
                    n += 1
    if num[-1]=='-':
        num = num.rstrip(num[-1])
    return num
print(list_num(s))
s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

d = {"five": 5, "thirteen":13, "two":2, "eleven":11, "seventeen":17, "one":1, "ten":10, "four":4, "eight":8, "nineteen":19}

s = {d[i] for i in s.split()}
print(s)

s = list(s)

res = 0
flag = True
for i in range(len(s)):
    if s[i]%2!=0:
        res += s[i]

    if i == len(s)-1:
        break

    if flag:
        print(f"{s[i]}*{s[i+1]} = {s[i]*s[i+1]}")
    else:
        print(f"{s[i]}+{s[i+1]} = {s[i]+s[i+1]}")
    flag = not flag

print(res)

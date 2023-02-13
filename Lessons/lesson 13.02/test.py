s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

s = list({{"five": 5, "thirteen":13, "two":2, "eleven":11, "seventeen":17, "one":1, "ten":10, "four":4, "eight":8, "nineteen":19}[s] for s in s.split()})
print(s)

s += [True, 0, 0]

while True:

    if s[s[-1]]%2!=0:
        s[-2] += s[s[-1]]

    if isinstance(s[s[-1]+1], bool):
        break

    if s[-3]:
        print(f"{s[s[-1]]}*{s[s[-1]+1]} = {s[s[-1]]*s[s[-1]+1]}")
    else:
        print(f"{s[s[-1]]}+{s[s[-1]+1]} = {s[s[-1]]+s[s[-1]+1]}")
    s[-3] = not s[-3]
    s[-1] += 1

print(s[-2])

# s = list(s)

# res = 0
# flag = True
# for i in range(len(s)):
#     if s[i]%2!=0:
#         res += s[i]

#     if i == len(s)-1:
#         break

#     if flag:
#         print(f"{s[i]}*{s[i+1]} = {s[i]*s[i+1]}")
#     else:
#         print(f"{s[i]}+{s[i+1]} = {s[i]+s[i+1]}")
#     flag = not flag

# print(res)

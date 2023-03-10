import re
text = input("Enter any text:\n")
l = re.findall(r"[A-Za-zа-яА-я\']+", text.lower())

# d = dict.fromkeys(l, 0)
# for i in l:
    # d[i] += 1

d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d |= {i: 1}

for key, value in d.items():
    print(f"{key}: {value}")

l = ('а','е','и','о','у','ы','э','ю','я')

user = input('enter world\n')
s = 0

for i in user:
    if i in l:
        s += 1
print(s)
l = ('а','е','и','о','у','ы','э','ю','я')

user = input('enter world\n')


for i in user:
    if i in l:
        continue
    print(i,end='')
print()
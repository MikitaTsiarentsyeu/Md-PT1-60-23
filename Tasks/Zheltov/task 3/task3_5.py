list = input('Enter numbers separated by spaces:\n').split()

list_11=[]
for i in list:
    if len(i)>5:
        list_11.append(i)
print(list_11)
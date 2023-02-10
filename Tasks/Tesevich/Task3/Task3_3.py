x = input ("Введите строку\n")
x = x.split(" ")
dict1 = {}
for i in x:
    r = x.count(i)
    dict1[i] = r
print ("Слова и их количество:", dict1)
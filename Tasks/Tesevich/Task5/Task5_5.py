#def get_ranges(a):
a = ("3 1 2 3 0 22 4 7 8 10 23 45 3 2 11 88")    

posl = []
a1 = []
itr = 1

a = a.split(" ")
for i in a:
    a1.append(int(i))

a1 = set(a1)
a1 = list(a1)
a1 = sorted(a1)
posl.append(a1[0])



for x in a1:
    if itr == len(a1): # не уверен в этой проверке, возможно стоило через ренжи
        
        break
    if x+1 == a1[itr]:
        posl.append("-")    
        itr =itr+1
    else:
        posl.append(x)
        posl.append(a1[itr])
        itr =itr+1
if posl[-2] == posl [-3]:
    del posl[-2] #это наверное костыль, но на послдней проверке возникает дубль если она без промежутков

posl = str(posl)
# for it in posl:
#     if it.isdigit():


# posl = set(posl)
# posl = list(posl)

print(posl)

#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
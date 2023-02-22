#def get_ranges(a):
data = [2, 3, 8, 9]  

def delete_doubles(y):
    rez = []
    it = 1
    for i in y:
        if it > len(y)-1:
            if y[-1] != y[-2]:
                rez.append(y[-1])
            break
        if i != y [it]:
            it = it +1
            rez.append(i)
        else:
            it = it +1
            continue
    return rez

def find_ranges(a1):
    posl = [a1[0]]
    itr = 1
    for x in a1:
        if itr == len(a1): # не уверен в этой проверке, как то не очень выглядит
            if posl[-1] == "-": # не уверен в этой проверке, как то не очень выглядит
                posl.append(a1[-1]) # не уверен в этой проверке, как то не очень выглядит
                break
            break
        if x+1 == a1[itr]:
            posl.append("-")    
            itr =itr+1
        else:
            posl.append(x)
            posl.append(a1[itr])
            itr =itr+1
    return posl

def get_ranges(data_1):
    
    rez = ''

    data_1 = sorted(data_1)
    data_1 = delete_doubles(data_1)
    data_1 = find_ranges(data_1)
    data_1 = delete_doubles(data_1)
    i= 0
    
    for data_1[i] in data_1:
        if i < (len(data_1)):
            if data_1[i] is data_1[-1]:
                rez = f'{rez}{data_1[i]}'
                i=i+1
                break
            elif isinstance(data_1[i],int)and isinstance(data_1[i+1],int):
                rez = f'{rez}{data_1[i]}, '
                i=i+1
            else:
                rez = f'{rez}{data_1[i]}'
                i=i+1       
    return rez

rezult = get_ranges(data)
print (rezult)


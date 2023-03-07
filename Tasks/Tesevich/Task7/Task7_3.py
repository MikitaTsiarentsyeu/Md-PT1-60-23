def even_sum(list_num):
    try:
        list_num2=[]
        for i in list_num:
            if int(i) != i:
                return "Invalid input type"
            if i%2 ==0:
                list_num2.append(i)
        return sum(list_num2)
    except TypeError:
        return "Invalid input type"
    
print(even_sum('123'))
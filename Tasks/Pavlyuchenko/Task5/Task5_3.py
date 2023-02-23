#3task
lst = ['home', 'work', 'is', 'done']
lst_2 = []

def more_than_5(x):
    for str in x:
        if len(str) > 5:
            lst_2.append(str)
    return(lst_2)

print(more_than_5(lst))

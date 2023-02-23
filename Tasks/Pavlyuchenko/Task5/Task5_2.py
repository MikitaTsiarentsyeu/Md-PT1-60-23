#2task
lst = ['home', 'work', 'is', 'done']
lst_2 = []

def reverse(x):
    for str in x:
        lst_2.append(str[::-1])
    return(lst_2[::-1])

print(reverse(lst))

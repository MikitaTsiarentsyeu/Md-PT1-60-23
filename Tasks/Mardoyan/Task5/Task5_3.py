list = str(input('Input a list of strings throught a space\n'))
list = list.split(' ')
x = []
def reserv_list(a):
    for i in a:
        if len(i) > 5:
            x.append(i)
    return x
print(reserv_list(list))
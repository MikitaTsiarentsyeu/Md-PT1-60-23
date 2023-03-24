def mass_func(q):
    try:
        x = [int(i) for i in q.split(' ')]
        return x
    except :
        return 'Invalid input type'

def num_func(sp):
    if len(sp)>1:
        try:
            z = [i for i in sp if i % 2 == 0]
            sum_list = sum(z)
            return sum_list
        except TypeError:
            return 'Invalid input type'
    else:
        return 'Invalid input type'
a = input('Input list throught "Space"\n')
massive = mass_func(a)
print(num_func(massive))

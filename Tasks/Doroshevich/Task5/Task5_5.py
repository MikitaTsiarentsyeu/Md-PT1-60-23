import random
def ranges_of_numbers(l):
    l1 = [l[0]]
    for i in range(1, len(l)-1):
        if type(l[i-1]) == int:
            if l[i] - l[i-1] == 1 and l[i+1] - l[i] == 1:
                l1 += ['']
            elif l[i] - l[i-1] == 1 and l[i+1] - l[i] != 1:
                l1 += [-l[i]]
            else:
                l1 += [', ', l[i]]
    if l[-1] - l[-2] == 1:
        l1 += [-l[-1]]
    else:
        l1 +=[', ', l[-1]]
    return ''.join([str(x) for x in l1])

list_of_numbers = list(set([random.randint(0, 20) for i in range(20)]))
print (f"Your ordered list of numbers without duplicates:\n{list_of_numbers}")
print(f"Your string with ranges for those numbers:\n{ranges_of_numbers(list_of_numbers)}")
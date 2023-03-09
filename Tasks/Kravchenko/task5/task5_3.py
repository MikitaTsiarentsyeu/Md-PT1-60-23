lst = input().split(";")

def long_strings(lst):
    new_lst = []
    for i in lst:
        if len(i) > 5:
            new_lst.append(i)
        else:
            continue
    return new_lst

print(long_strings(lst))

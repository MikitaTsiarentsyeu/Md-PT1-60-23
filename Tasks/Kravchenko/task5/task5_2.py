lst = input().split()

def reverse_list (lst):
    rev_lst = lst[::-1]
    rev_lst_str = []
    for i in rev_lst:
        i = i[::-1]
        rev_lst_str.append(i)

    return rev_lst_str

print(reverse_list(lst))

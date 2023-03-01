import random

def merge_sort(l):
    
    if len(l) == 1:
        return l
    return compare_rec(merge_sort(l[:len(l)//2]), merge_sort(l[len(l)//2:]))

def compare_rec(l1, l2):

    if l1 == []:
        return l2

    if l2 == []:
        return l1

    return [l1[0]] + compare_rec(l1[1:], l2) if l1[0] <= l2[0] else [l2[0]] + compare_rec(l1, l2[1:])


def random_list(length, l=[]):

    if len(l) == length:
        return l

    return [random.randint(0, 50)] + random_list(length-1, l[:length - 1])


random_list = random_list(16)
print(random_list, '\n', merge_sort(random_list))

import random


# 1st way
def ranges_of_numbers1(l):
    l1 = [l[0]]
    for i in range(1, len(l)-1):
        if l[i] - l[i-1] == 1 and l[i+1] - l[i] == 1:
            continue
        elif l[i] - l[i-1] == 1 and l[i+1] - l[i] != 1:
            l1 += [-l[i]]
        else:
            l1 += [', ', l[i]]
    l1 += [-l[-1]] if l[-1] - l[-2] == 1 else [', ', l[-1]]
    return ''.join([str(x) for x in l1])


# 2nd way
def ranges_of_numbers2(l):
    s = f'{l[0]}'
    for i in range(1, len(l)-1):
        if l[i] - l[i-1] == 1 and l[i+1] - l[i] == 1:
            continue
        elif l[i] - l[i-1] == 1 and l[i+1] - l[i] != 1:
            s += f'{-l[i]}'
        else:
            s += f', {l[i]}'
    s += f'{-l[-1]}' if l[-1] - l[-2] == 1 else f', {l[-1]}'
    return s


list_of_numbers = list(set([random.randint(0, 20) for i in range(20)]))
print(f"Your ordered list of numbers without duplicates:\n{list_of_numbers}")
print(
    f"Your string with ranges for those numbers(1st way):\n{ranges_of_numbers1(list_of_numbers)}")
print(
    f"Your string with ranges for those numbers(2nd way):\n{ranges_of_numbers2(list_of_numbers)}")

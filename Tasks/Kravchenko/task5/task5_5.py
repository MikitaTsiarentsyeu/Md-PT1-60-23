l = input().split()
lst = []
for val in l:
    val = int(val)
    lst.append(val)

ranges = []
def get_ranges(lst):
    start = lst [0]
    for i in range(len(lst)):
        if lst[i] != lst[-1] and lst[i] + 1 != lst[i+1]:
            finish = lst[i]
            func2(start, finish)
            start = lst[i+1]
        elif lst[i] == lst[-1]:
            finish = lst[i]
            func2(start, finish)           

    ranges_str = ", ".join(ranges)
    return ranges_str

def func2(start,finish): 
    s = set()
    s.add(start)
    s.add(finish)
    if len(s) == 1:
        ranges.append(f"{min(s)}")
    else:
        ranges.append(f"{min(s)}-{max(s)}")

                               
print(get_ranges(lst))
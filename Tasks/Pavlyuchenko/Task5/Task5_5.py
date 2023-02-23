#5task
lst = [1, 2, 3, 5, 6, 10, 12, 14, 15, 16]

def line(x):
    seq = []
    final = []
    last = 0
    for i, val in enumerate(x):
        if last + 1 == val or i == 0:
            seq.append(val)
            last = val
        else:
            if len(seq) > 1:
               final.append(str(seq[0]) + '-' + str(seq[len(seq)-1]))
            else:
               final.append(str(seq[0]))
            seq = []
            seq.append(val)
            last = val
        if i == len(x) - 1:
            if len(seq) > 1:
                final.append(str(seq[0]) + '-' + str(seq[len(seq)-1]))
            else:
                final.append(str(seq[0]))
    final_str = ', '.join(map(str, final))
    return final_str

print(line(lst))
    

def count_num(val, symb, count = 0):
    if val[0] == symb:
        count += 1 
    if len(val) == 1:
        return count
    return count_num(val[1:], symb, count)

print(count_num('test', 't'))

# the second way
def count_num(val, symb, count = 0):
    if val[0] == symb:
        count = 1
    else:
        count = 0 
    if len(val) == 1:
        return count
    return count + count_num(val[1:], symb, count)

print(count_num('test', 't'))
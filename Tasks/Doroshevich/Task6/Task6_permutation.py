def permutation(s):
    
    if len(s) == 1:
        return [s]

    l = []

    for i in s:
        for j in permutation(s.replace(i, '', 1)):
            if i+j not in l:
                l.append(i + j) 

    return l

print(permutation('abba'))





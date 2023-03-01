def permutation(s):
    if len(s) == 1:
        return [s]

    l = []
    for i in range(len(s)):
        for j in permutation(s.replace(s[i],'', 1)):
            l.append(s[i] + j)

    return sorted(list(set(l)))

print(permutation('brain'))





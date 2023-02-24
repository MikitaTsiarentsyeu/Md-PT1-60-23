def get_ranges(s):
    s_new=[]
    res = []
    for i in range(len(s)):
        if s[i] == s[len(s)-1]:
            if s[i] - s[i-1] > 1 or len(s)==1:
                res.append(f'{s[i]}')
            break
        if s[i+1] - s[i] == 1 or s[i] - s[i-1] == 1:
            s_new.append(s[i])
            if s[i+1] == s[len(s)-1] and s[i+1] - s[i] == 1:
                s_new.append(s[i+1])
            if s[i+1] - s[i] > 1 or s[i+1] == s[len(s)-1]:
                res.append(f'{min(s_new)} - {max(s_new)}')
                s_new=[]
        elif s[i+1] - s[i] > 1:
            res.append(f'{s[i]}')
    return(res)


assert get_ranges([4,7,10]) == ['4', '7', '10']
assert get_ranges([2, 3, 8, 9]) == ['2 - 3', '8 - 9']
assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == ['0 - 4', '7 - 8', '10']
assert get_ranges([1]) == ['1']
def rev_list(s):
    # new_s = []
    # for i in s:
    #     new_s.append(i[::-1])
    new_s = [s[::-1] for s in s]
    return(new_s)

s = ['test', 'asd']
print(s)
print(rev_list(s))


# def rev_list(s):
#     new_s = ''
#     for i in range(len(s)-1,-1,-1):
#         new_s += s[i]
#     return(new_s)

# print(rev_list('test asd'))
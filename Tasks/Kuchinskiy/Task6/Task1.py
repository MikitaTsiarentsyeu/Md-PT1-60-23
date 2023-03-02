# def level(n=1):
#     if n == 5:
#         return
#     print(f"{'    '*(n-1)}level{n} started")
#     level(n+1)
#     print(f"{'    '*(n-1)}level{n} finished")

# level()
# print('the end')

def rev_str(val):
    if len(val) == 1:
        return val
    return val[-1] + rev_str(val[:-1])

print(rev_str(input('enter string\n')))

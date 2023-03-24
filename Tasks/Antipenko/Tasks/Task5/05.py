'''Write a function that takes an ordered list of numbers without duplicates and returns
a string with ranges for those numbers, check the example below:
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"'''


def nums(lst):
    res = str(lst[0])
    for n in range(len(lst) - 1):
        if lst[n] + 1 == lst[n + 1]:
            if res[-1] != '-':
                res += '-'
        else:
            if f'{lst[n]}' not in res:
                res += f'{lst[n]}, {lst[n + 1]}'
            else:
                res += f', {lst[n + 1]}'
    return res


print(nums([0, 2, 3, 4, 5, 7, 8, 10, 12, 14, 15, 16, 18]))

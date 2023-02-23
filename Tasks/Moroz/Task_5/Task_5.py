
# 1. Write a function that takes two integers as arguments and returns their sum.

""" Just wanted to practice preventing/handling errors, let me know if that makes sense pls =)"""


def sum_func(a: int, b: int) -> int:
    assert isinstance(a+b, int), "The arguments can only be int "
    return a+b


def new_sum_func(*args: int, default=0) -> int:
    try:
        return int(sum(args))
    except TypeError:
        print("The arguments can only be numbers")
        return default


print(sum_func(True, -2))
print(new_sum_func(1, 2.0, "False"))


# 2. Write a function that takes a list of strings as an argument and returns a new
# list of strings that are all reversed.


def str_reversion(lst: list) -> list:
    return [lst[i][::-1] for i in range(len(lst))]


print(str_reversion(["list", 'cat', '1', '']))


# 3. Write a function that takes a list of strings as an argument and returns a new list
# with all the strings that have a length greater than 5.


def greater_than_five(lst: list) -> list:
    return [elem for elem in lst if len(elem) > 5]


print(greater_than_five(["hello", "world", "", "gfhjkl;'lkjhgfc"]))


# 4. Write a function that takes a string as an argument and returns two numbers,
# first for count of lower case symbols, second for count of the upper case symbols in the initial string.


def str_symbols_count(arg: str) -> str:
    lst = [1 if elem.islower() else 2 if elem.isupper() else 0 for elem in arg]
    return f"count of lower case symbols: {lst.count(1)} \ncount of the upper case symbols: {lst.count(2)}"


print(str_symbols_count("LalaBla bjb !!!"))



# 5. Write a function that takes an ordered list of numbers without duplicates and returns a
# string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


"""This one was a bit challenging and I came up with the following idea, 
definitely would love to see more elegant way"""

lst = [0, 1, 2, 3, 4, 7, 8, 10]

def get_ranges(lst: list) -> str:
    b = []
    sublst = []
    prev_n = -1
    for n in lst:
        if prev_n+1 != n:
            b = sublst_checker(sublst, b)
            sublst = []
        sublst.append(n)
        prev_n = n
    b = sublst_checker(sublst, b)
    return ", ".join(b)

def sublst_checker(sublst: list, b: list):
    if len(sublst) > 1:
        b.append(f"{min(sublst)}-{max(sublst)}")
    elif len(sublst) == 1:
        b.append(f"{min(sublst)}")
    return b

print(get_ranges(lst))



def sum_of_even(l):
    try:
        return sum([x for x in l if not x % 2])
    except TypeError:
        return "Invalid input type"


print(sum_of_even(5))

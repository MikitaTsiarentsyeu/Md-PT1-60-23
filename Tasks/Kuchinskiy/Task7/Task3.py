try:
    s = input("enter list of nuber\n")
    if len(s) < 3:
        raise TypeError("list length  is too small")

    l = list(map(int, s.split()))

    new_l = list(filter(lambda x: x%2==0, l))

    print(sum(new_l))

except ValueError as e:
    print(e)
except TypeError as e:
    print(e)


# def sum_even(l):
#     try:
#         l = list(map(int, s.split()))
#         new_l = list(filter(lambda x: x%2==0, l))
#         print(sum(new_l))
#     except ValueError as e:
#         print(e)
#         return False

# try:
#     s = input("enter list of nuber\n")
#     if len(s) < 3:
#         raise TypeError("list length  is too small")
#     sum_even(s)

# except TypeError as e:
#     print(e)
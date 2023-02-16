# for i in range(1, 101):
#     f = ""
#     b = ""
#     if i%3==0:
#         f="FIZZ"
#     if i%5==0:
#         b="BUZZ"
#     res = f+b
#     if res:
#         print(f+b)
#     else:
#         print(i)

print([("FIZZ"*(i%3==0))+("BUZZ"*(i%5==0)) or i for i in range(1, 101)])
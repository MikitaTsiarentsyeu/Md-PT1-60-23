
def sum_int(l):
    try:
        l_num = []
        for i in l:
            if int(i) != i:
                return "Invalid input type"
            if i % 2 == 0:
                l_num.append(i)
                return sum(l_num)
    except TypeError:
        print("Invalid input type")


print(sum_int('123'))

def even(nombers):
    res = 0
    for i in nombers:
        try:
            i == int(i)
        except ValueError:
            return "Invalid input type"
        if int(i) % 2 == 0:
           print(res,"+",int(i))
           res = res + int(i)
    return  res
print(even(input("ваши числа")))
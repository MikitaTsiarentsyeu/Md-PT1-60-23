def cash_func (funk, cash = {}):
    def wrapper (x,y):
            args = f"{x},{y}"
            rez = cash.get(args)
            if rez == None:
                cash[args]=funk(x,y)
                return funk(x,y)
            else:
                return cash.get(args)
    return wrapper




@cash_func
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except:
        return "Invalid data input"


print(divide(1,2))
print(divide(1,2))
print(divide(2,2))
print(divide(1,2))
print(divide(2,2))
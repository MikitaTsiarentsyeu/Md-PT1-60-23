def fibonachi_func (con, number2 = 1, number1 = 0 ):
   
    if con == 0:
        return number1
    else:
        return fibonachi_func((con - 1), number2 = number2+number1, number1 = number2)

print(fibonachi_func(2))

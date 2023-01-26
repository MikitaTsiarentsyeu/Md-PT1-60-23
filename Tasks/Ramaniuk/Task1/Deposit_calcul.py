print("Hello! Input your value of amount:")
P = int(input())
if P!=0:
    print("Input the term of your deposit in years, please:")
else:
    print("As you make your bed, so you must lie in it. The amount on your account will be 0.")
t = int(input())
if t!=0:
    print("Input the annual percentage, please:")
else:
    print("As you make your bed, so you must lie in it. The amount on your account will be 0.")
I = int(input())
if I!=0:
    S = P + (P * I / 100 * t)  #There are a lot of formulas for calculating, but I see no reason to use them if the task is that the input will be the amount, the term in years and the annual percentage.
    print("The amount on your account will be", S, "BYN.")
else:
    print("As you make your bed, so you must lie in it. The amount on your account will be 0.")
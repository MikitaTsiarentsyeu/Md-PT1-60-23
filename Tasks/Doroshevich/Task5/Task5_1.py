def func_sum(term1, term2):
    return term1 + term2


while True:
    a, b = input("Enter 1st argument:\n"), input("Enter 2nd argument:\n")
    if a.isnumeric() and b.isnumeric():
        print(f"Your result:\n{func_sum(int(a), int(b))}")
        break
    else:
        print("Wrong data. Please enter integers!")
